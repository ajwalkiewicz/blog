"""Copy posts from Obsidian to hugo page"""
import shutil
import sys
from pathlib import Path
from typing import Literal, TypeGuard

from replace import transform_file

def copy(source: Path, dest: Path, mode: Literal["image", "post"]) -> list[Path]:
    # TODO: Refactor it to something more optimal

    source_files = {
        path: path.stat().st_mtime for path in source.iterdir() if path.is_file()
    }
    dest_files = {
        path: path.stat().st_mtime for path in dest.iterdir() if path.is_file()
    }

    copied_files: list[Path] = []

    for file, timestamp in source_files.items():
        if file in dest_files:
            if timestamp <= dest_files[file]:
                continue

        if mode == "post":
            copied_files.append(transform_file(file, dest / file.name))
        else:
            copied_files.append(Path(shutil.copy(file, dest)))
    
    return copied_files

def _is_mode_valid(mode: str) -> TypeGuard[Literal["image", "post"]]:
    return mode in ["image", "post"]

def main() -> None:
    mode = sys.argv[1]
    source = Path(sys.argv[2])
    destination = Path(sys.argv[3])

    if not _is_mode_valid(mode):
        raise ValueError("Incorrect mode")
    
    copy(source, destination, mode)


if __name__ == "__main__":
    main()