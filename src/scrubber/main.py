from pathlib import Path
from argparse import ArgumentParser

from .scrubber import Scrubber

parser = ArgumentParser(
    prog='Log Scrubber',
    description="Clean logs containing sensitive data. Only the root dir name is different when `src` is a directory. Filenames don't change in these cases.",
)
parser.add_argument('src', help='src can be a file or directory. Make dst the same type, but with your desired name for clean logs')
parser.add_argument('dst')
parser.add_argument('--encoding', default='utf-8')
parser.add_argument('--ignore-case', action='store_true', help='Make regex parsing case-insensitive')
args = parser.parse_args()


def main(pairs):
    src = Path(args.src)
    dst = Path(args.dst)
    encoding = args.encoding
    ignore = args.ignore_case

    scrubber = Scrubber(src, dst, pairs, encoding, ignore_case=ignore)
    scrubber.tree_walker()

    if src.is_file():
        scrubber.parse_and_replace(src, dst)

    else:
        scrubber.tree_walker()


if __name__ == '__main__':
    import re
    pairs = [
        (re.compile(r"a"), "HELLO"),
        (re.compile(r"b"), "GOODBYE"),
        (re.compile(r"c"), "ADIOS"),
        ]
    main(pairs)