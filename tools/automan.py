#! /usr/bin/env python3

# [AutoMan ~ 0.1]
# Author: NateMount (@NateMount)

# === Imports
from sys import argv

# === AutoMan Class

class AutoMan:

    def __init__(self):
        self.log = lambda *_: None
    
    def build_from_arr(self, site_array:list[str]) -> None:
        pass

    def build_from_tag(self, tag_array:list[str]) -> None:
        pass

    def exec(self, command:str) -> None:
        match command.lower():
            case 'build':
                if len(argv) < 3:
                    print("[AutoMan::Err ~]: No build list or list of sites provided")
                    return
                
                if argv[3].startswith('@'):
                    try:
                        site_arr:list[str] = open(argv[3][1:], 'r').read().split('\n')
                    except FileNotFoundError:
                        self.log("Err", f"Cannot open file @[{argv[3][1:]}]")
                        return
                else:
                    site_arr:list[str] = argv[3:]
                
                self.build_from_arr(site_arr)

            case 'new':
                if len(argv) < 3:
                    print("[AutoMan::Warn ~]: No tags provided, building default list")
                    tags:list[str] = []
                else:
                    tags:list[str] = argv[3:]
                
                self.build_from_tag(tags)

            case 'tags':
                print("[AutoMan::IDX ~]: Tags")
                # Display availible tags

            case _:
                self.log("Err", f"Command {command} not recognized")
                print("[AutoMan ~]:\n\nUsage:\n\tpython3 automan.py <command> @<sitelist_file> [/v]")
                return


def main() -> None:

    if len(argv) < 2:
        print("[AutoMan ~]:\n\nUsage:\n\tpython3 automan.py <command> @<sitelist_file> [/v]")
        return

    automan = AutoMan()
    if '/v' in argv:
        automan.log = lambda status, msg: print(f"[AutoMan::{status} ~]: {msg}")
    
    automan.exec(argv[1])

if __name__ == '__main__':
    AutoMan()