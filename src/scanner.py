# [PyHund::Scanner ~]

# === Imports

from json import load
from src import args
from threading import Lock, Thread
from requests import get, RequestException, Response

# === Globals
LOCK:Lock = Lock()

# === PyHund Scanner Class

class PyHundScanner:

    def __init__(self):
        self.manifest:dict = {}
        self.scan_data:dict = {}

        self.log = lambda *msg : None
    
    def run(self, user_instances:list[str], thread_count:int):
        """
        Executes scan of all provided user instances
        
        :param user_instances: Iterable collection of strings, each representing a single user instance
        :param thread_count: Maximum number of threads to be allocated to scan execution
        """

        self.log(f"Starting scan with Users[{len(user_instances)}] & ThreadCount[{thread_count}]")

        for user_instance in user_instances: self._scan_instance(user_instance=user_instance)

    def load_manifest(self, manifest_path:str):
        """
        Attempts to load manifest site data from specified path
        
        :param manifest_path: Full path to the desired manifest file (json)
        """

        try:
            self.manifest = load(open(manifest_path, 'r'))
        except FileNotFoundError:
            print(f"[PyHund.Err ~]: Cannot load manifest with path [{manifest_path}]")
            exit(-1)
    
    def _scan_instance(self, user_instance:str) -> None:
        """
        Scans an array of sites derived from Manifest for selected user instance
        
        :param user_instance: String representing targeted user instance
        """

        self.scan_data[user_instance] = {}

        site_blocks:list[list[str]] = []
        chunk_size:int = len(self.manifest)//args.threads
        site_names:list[str] = [ site for site in self.manifest ]

        for i in range(args.threads-1):
            site_blocks.append(site_names[chunk_size*i:chunk_size*(i+1)])
        site_blocks.append(site_names[chunk_size*args.threads:])

        threads = [
            Thread(
                target=self._scan_site_block, 
                args=(user_instance, block)
            ) for block in site_blocks
            if len(block) > 0
        ]

        [t.start() for t in threads]
        [t.join() for t in threads]

        print(self.scan_data)
    
    @staticmethod
    def _validate_response(response_data:Response, user_instance:str, verification_method:str, verification_keys:dict) -> str:
        """
        Uses established verification methods and keys to tag this connection as valid / invalid / unknown
        
        :param response_data: Response data from site connection
        :param user_instance: User instance used for search
        :param verification_method: Method used to identify if user does exist on site
        :param verification_keys: Mapping of 'invalid' and 'valid' status to their respective keys based on verification method
        :return: Valid / Invalid / Unknown 
        """


        match verification_method:
            case 'status-code':
                if response_data.status_code == verification_keys['valid']:
                    return 'Valid' 
                return 'Invalid'

            case 'url':
                if response_data.url.replace(user_instance, '@@@@@') == verification_keys['valid']:
                    return 'Valid'
                return 'Invalid'

            case 'length':
                response_len:int = len(response_data.text.replace(user_instance, '@@@@@'))
                if abs(response_len - verification_keys['valid']) < abs(response_len - verification_keys['invalid']):
                    return 'Valid'
                return 'Invalid'

            case 'key-string':
                if verification_keys['invalid'] in response_data.text.replace(user_instance, '@@@@@'):
                    return 'Invalid'
                return 'Valid'

            case _:
                return 'Unknown'



    def _scan_site_block(self, user_instance:str, site_block:list[str]) -> None:
        """
        Allows for fragmentation of scan space into threaded blocks, allowinf for faster 
        compute speeds
        
        :param user_instance: String representing the user instance to be applied
        :param site_block: List containing slice of all sites to be scanned
        """

        print(site_block)

        for site_name in site_block:
            self.log(f"Scanning: [{user_instance}@{site_name}]")
            site_metadata:dict = self.manifest[site_name]
            try:
                response_data:Response = get(
                    site_metadata['url'].format(user_instance),
                    headers=site_metadata['headers'],
                    cookies=site_metadata['cookies']
                )
            except RequestException as err:
                self.log(f"Error Encountered:\n\tError: {err}\n\tTarget: {site_metadata['url'].format(user_instance)}")
                self.scan_data[user_instance][site_name] = ('Error', 'Cannot Connect to Site')
                continue

            self.scan_data[user_instance][site_name] = (
                self._validate_response(
                    response_data=response_data, 
                    user_instance=user_instance,
                    verification_method=site_metadata['check-type'], 
                    verification_keys=site_metadata['criteria']
                ),
                site_metadata['url'].format(user_instance),
                response_data.status_code,
                site_metadata['check-type'],
                site_metadata['criteria']
            )