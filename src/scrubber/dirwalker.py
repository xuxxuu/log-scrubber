from pathlib import Path
from .scrubber import parse_and_replace, RE_PAIRS

target_dir = Path("./logs")
destination_dir = Path("./clean_logs")


def tree_walker(src_dir: Path, dst_dir: Path):
    for root, _, files in src_dir.walk():
        relative_root = root.relative_to(src_dir)
        destination_path = dst_dir / relative_root
        destination_path.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_file = root / file
            dst_file = destination_path / file
            parse_and_replace(src_file, dst_file, RE_PAIRS) 