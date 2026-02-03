# [PyHund | Revision 8]
# Author(s): Nate Mount ( @NateMount )
# Version: 8.0.0 - InDev

# === Imports

from src import args
from src.scanner import PyHundScanner

# === Main Execution

def main():
    pyhund_scanner:PyHundScanner = PyHundScanner()
    if args.verbose:
        pyhund_scanner.log = lambda *msg: print(f"[PyHund.Scanner ~]: {msg}")

    pyhund_scanner.load_manifest(args.manifest)
    pyhund_scanner.run(args.usernames, args.threads or 3)

if __name__ == '__main__':
    main()