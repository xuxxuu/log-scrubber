import re
from pathlib import Path
from typing import Sequence


default_encoding = 'ISO-8859-1'

class Scrubber:
    def __init__(self, src_path: Path, dst_path: Path, pairs: Sequence[tuple[re.Pattern, str]], encoding: str | None, ignore_case: bool = False) -> None:
        self.src_path = src_path
        self.dst_path = dst_path
        self.pairs = pairs
        self.encoding = encoding
        self.ignore_case = ignore_case

    def parse_and_replace(self, src_file, dst_file):
        try:
            with open(src_file, 'r', encoding=self.encoding) as src, open(dst_file, 'w', encoding=self.encoding) as dst:
                for line in src.readlines():
                    for pattern, replacement in self.pairs:
                        if self.ignore_case:
                            line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                        else:
                            line = re.sub(pattern, replacement, line)
                    dst.write(line)
        except LookupError:
            print("Encoding provided does not exist, or is not supported. Please provide a valid encoding.")

    def tree_walker(self):
        for root, _, files in self.src_path.walk():
            relative_root = root.relative_to(self.src_path)
            destination_path = self.dst_path / relative_root
            destination_path.mkdir(parents=True, exist_ok=True)

            for file in files:
                src_file = root / file
                dst_file = destination_path / file
                self.parse_and_replace(src_file, dst_file)