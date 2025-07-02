import re
from pathlib import Path


RE_PAIRS = [
    (re.compile(r"a"), r"HELLO"),
    (re.compile(r"b"), r"GOODBYE"),
    (re.compile(r"c"), r"BONJOUR"),
    (re.compile(r"d"), r"ALOHA"),
]


def parse_and_replace(src_file: Path, dst_file: Path, pairs: list[tuple[re.Pattern, str]], ignore_case: bool = False):
    with open(src_file, 'r', encoding='ISO-8859-1') as src, open(dst_file, 'w', encoding='ISO-8859-1') as dst:
        for line in src.readlines():
            for pattern, replacement in pairs:
                match ignore_case:
                    case True:
                        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                    case False:
                        line = re.sub(pattern, replacement, line)
                # if ignore_case:
                #     line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                # else:
                #     line = re.sub(pattern, replacement, line)
            dst.write(line)