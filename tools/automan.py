#! /usr/bin/env python3

# [AutoMan ~ 0.1]
# Author: NateMount (@NateMount)

# === Imports
from sys import argv

# === AutoMan Class

class AutoMan:

    def __init__(self):
        self.log = lambda msg: None
    
    def exec(self, command:str) -> None:
        match command.lower():
            case 'build':
                pass
            case 'new':
                pass
            case 'tags':
                pass
            case _:
                self.log(f"[AutoMan:Err ~]: Command {command} not recognized")
                print("[AutoMan ~]:\n\nUsage:\n\tpython3 automan.py <command> @<sitelist_file> [/v]")
                return




def main() -> None:

    if len(argv) < 2:
        print("[AutoMan ~]:\n\nUsage:\n\tpython3 automan.py <command> @<sitelist_file> [/v]")
        return

    automan = AutoMan()
    if '/v' in argv:
        automan.log = lambda msg: print(f"[AutoMan::Info ~]: {msg}")
    
    automan.exec(argv[1])

if __name__ == '__main__':
    AutoMan()