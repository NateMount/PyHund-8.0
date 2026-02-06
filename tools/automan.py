#! /usr/bin/env python3

# [AutoMan ~ 0.1]
# Author: NateMount (@NateMount)

# === Imports
from sys import argv
#from tools.pyhunter import PyHunter

# === Globals

# Tags: 
#   - Social (social media)
#   - Finance (financial transactions / stock or crypto trading / crypto wallet)
#   - Education (online learning / training platforms)
#   - Professional (business accounts)
#   - Forum (online form / chat room)
#   - Adult (pornographic / dating content)
#   - Communication (online messaging platforms)

TAG_MANIFEST:tuple = (
    (("social", "finance"), "https://venmo.com/u/{}"),
    (("professional", "social"), "https://www.linkedin.com/in/{}/")
)

# === AutoMan Class

class AutoMan:

    def __init__(self):
        self.log = lambda _, __: None
    
    def build_from_arr(self, site_array:list[str]) -> None:
        
        for site_element in site_array:
            if '{}' not in site_element:
                self.log('Warn', f"URL [{site_element}] does not contain formatting braces, {{}} - Skipping")
                continue

    def build_from_tag(self, tag_array:list[str]) -> None:
        
        site_array:list[str] = []
        [
            [ site_array.append(site[1]) for tag in site[0] if tag in tag_array ] 
        for site in TAG_MANIFEST ]

        print(site_array)

        self.build_from_arr(site_array=site_array)

    def exec(self, command:str) -> None:
        match command.lower():
            case 'build':
                if len(argv) < 3:
                    print("[AutoMan::Err ~]: No build list or list of sites provided")
                    return
                
                if argv[2].startswith('@'):
                    try:
                        site_arr:list[str] = open(argv[2][1:], 'r').read().split('\n')
                    except FileNotFoundError:
                        self.log("Err", f"Cannot open file @[{argv[2][1:]}]")
                        return
                else:
                    site_arr:list[str] = argv[2:]
                
                self.build_from_arr(site_arr)

            case 'new':
                if len(argv) < 3:
                    print("[AutoMan::Warn ~]: No tags provided, building default list")
                    self.build_from_arr([ site[1] for site in TAG_MANIFEST ])
                    return
                else:
                    self.build_from_tag(argv[2:])

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
    main()