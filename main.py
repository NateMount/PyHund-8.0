# [PyHund | Revision 8]
# Author(s): Nate Mount ( @NateMount )
# Version: 8.0.0 - InDev

# === Imports

from src import args
from src.scanner import PyHundScanner
from src.reporter import PyHundReporter

# === Main Execution

def main():
    pyhund_scanner:PyHundScanner = PyHundScanner()
    if args.verbose:
        pyhund_scanner.log = lambda msg: print(f"[PyHund ~]: {msg}")

    pyhund_scanner.load_manifest(args.manifest)
    raw_scan_data:dict = pyhund_scanner.run(args.usernames, args.threads or 3)
    PyHundReporter().build_report(raw_scan_data)

if __name__ == '__main__':
    main()