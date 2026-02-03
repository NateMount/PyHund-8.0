# [PyHund::Scanner ~]

# === Imports

from json import load
from threading import Lock, Thread

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
        Executes scan of all provided UserInstances
        
        :param self: Description
        :param user_instances: Iterable collection of strings, each representing a single user instance
        :param thread_count: Maximum number of threads to be allocated to scan execution
        """

        self.log(f"Starting scan with Users[{len(user_instances)}] & ThreadCount[{thread_count}]")

        for user_instance in user_instances:
            self._scan_instance(user_instance=user_instance)

    def load_manifest(self, manifest_path:str):
        try:
            self.manifest = load(open(manifest_path, 'r'))
        except FileNotFoundError:
            print(f"[PyHund.Err ~]: Cannot load manifest with path [{manifest_path}]")
            exit(-1)
    
    def _scan_instance(self, user_instance:str) -> None:
