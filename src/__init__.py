# [PyHund::src - init]

# === Imports
from argparse import ArgumentParser

# === Functions

def resolve_usernames(usernames:list[str]):
    """
    Used to unpack usernames stored in files, passed in by user in the form of @<filepath>
    :param usernames: List of the username values passed in by user through command-line arguments
    :yields str: Next username in file or argument sequence
    """
    for user in usernames:
        if user.startswith('@'):
            try:
                with open(user[1:], 'r') as f:
                    # Yield valid lines from file, stripping whitespace
                    yield from ( line.strip() for line in f if line.strip() and not line.lstrip().startswith('#'))
                continue
            except FileNotFoundError:
                pass # Treat as a literal username (e.g. @TwitterHandle)
        yield user

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
PARSER.add_argument('/manifest', '/m', help="Sets the manifest to be used for program execution", default='./manifest.json')

# Pre-build args 
args = PARSER.parse_args()

# Unpack passed in user files
args.usernames = list(resolve_usernames(args.usernames))