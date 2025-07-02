import re
from pathlib import Path
from argparse import ArgumentParser

from .dirwalker import tree_walker
from .scrubber import parse_and_replace, RE_PAIRS

parser = ArgumentParser(
    prog="Log Scrubber",
    description="Clean logs containing sensitive data. Only the root dir name is different when `src` is a directory. Filenames don't change in these cases.",
)
parser.add_argument('src', help="src can be a file or directory. Make dst the same type, but with your desired name for clean logs")
parser.add_argument('dst')
parser.add_argument('--ignore-case', action='store_true', help="Make regex parsing case-insensitive")
args = parser.parse_args()


def main():
    src = Path(args.src)
    dst = Path(args.dst)
    ignore = args.ignore_case
    print(ignore)
    exit()

    if src.is_file():
        parse_and_replace(src, dst, RE_PAIRS, ignore_case=ignore)

    else:
        tree_walker(src, dst, ignore_case=ignore)