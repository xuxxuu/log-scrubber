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
args = parser.parse_args()


def main():
    src = Path(args.src)
    dst = Path(args.dst)
    if src.is_file():
        parse_and_replace(src, dst, RE_PAIRS)
    else:
        tree_walker(src, dst)