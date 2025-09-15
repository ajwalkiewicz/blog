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
        # TODO: This doesn't make sense, cause I'm comparing different paths
        # and it's is always false, so at the end I'm coping anyway everything.
        if file in dest_files:
            if timestamp <= dest_files[file]:
                print("Skipped:", file)
                continue

        if mode == "post":
            copied_files.append(transform_file(file, dest / file.name))
        
        if mode == "image":
            new_name = file.name.split()[2]
            copied_files.append(Path(shutil.copy(file, dest / new_name)))
    
        print("Copied:", file)

    return copied_files

def _is_mode_valid(mode: str) -> TypeGuard[Literal["image", "post"]]:
    return mode in ["image", "post"]

def main() -> None:
    # mode = sys.argv[1]
    # source = Path(sys.argv[2])
    # destination = Path(sys.argv[3])

    # if not _is_mode_valid(mode):
    #     raise ValueError("Incorrect mode")
    
    # copy(source, destination, mode)

    # TODO: put it in another script?
    copy(Path("obsidian/_images"), Path("page/content/posts/images"), "image")
    copy(Path("obsidian/posts"), Path("page/content/posts"), "post")

if __name__ == "__main__":
    main()