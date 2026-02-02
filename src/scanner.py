# [PyHund::Scanner ~]

# === Imports

from json import load

# === PyHund Scanner Class

class PyHundScanner:

    def __init__(self, targets:list[str]):
        self.targets:list[str] = targets
        self.manifest:dict = {}

        self.log = lambda *msg : None
    
    def run(self, usernames:list[str], thread_count:int = 1):

        self.log(f"Starting scan with Users[{len(usernames)}] & ThreadCount[{thread_count}]")

        for username in usernames:
            pass

    def load_manifest(self, manifest_path:str):
        try:
            self.manifest = load(open(manifest_path, 'r'))
        except FileNotFoundError:
            print(f"[PyHund.Err ~]: Cannot load manifest with path [{manifest_path}]")
            exit(-1)