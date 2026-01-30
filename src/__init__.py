# [PyHund::src - init]

# === Imports
from argparse import ArgumentParser

# === Parser Setup

# Build Parser
PARSER:ArgumentParser = ArgumentParser(
    prog="PyHund",
    description="Adaptive and modular OSINT web-scraping tool used to detect user-instances across the internet",
    prefix_chars='/'
)

# Add Args
PARSER.add_argument('usernames', nargs='+')
PARSER.add_argument('/verbose', '/v', help="Enable verbose output for program execution", action='store_true')
PARSER.add_argument('/output', '/o', help="Sets expected output file in the form of name.ext", default='Report.txt')
PARSER.add_argument('/threads', '/t', help="Set maximum number of threads to be issued during program execution", type=int, default=3)
PARSER.add_argument('/noerr', '/n', help="Strip any misses & exceptions that occur during program execution", action="store_true")

# Pre-build args 
args = PARSER.parse_args()

if args.usernames[0].startswith('@'):
    try:
        with open(args.usernames[0][1:], 'r') as f:
            args.usernames = f.read().split('\n')
    except FileNotFoundError:
        print(f"[PyHund::Err ~]: File [{args.usernames[0][1:]}] Not Found")