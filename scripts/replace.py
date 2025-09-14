"""Replace Obsidian image links into Hugo links format"""
import sys
from pathlib import Path

__author__ = "Adam Walkiewicz"
__version__ = "0.0.1"

def is_obsidian_link(line: str) -> bool:
    """Check if passed link is in Obsidian format
    
    Example:
        >>> is_obsidian_link("![[Pasted image 20250831143608.png]]")
        True
        >>> is_obsidian_link("![image](Pasted image 20250831143608.png)")
        False
    """
    line = line.strip()
    return line.startswith("![[") and line.endswith("]]")

def transform_link(line: str, path: str | None = None) -> str:
    """Transform link from Obsidian to Hugo format.
    
    Examples:
        >>> link = "![[Pasted image 20250831143608.png]]"
        >>> transform_link(link)
        '![image](/20250831143608.png)'
        >>> transform_link(link, "/posts/images")
        '![image](/posts/images/20250831143608.png)'
    """
    filename = line.strip().split()[2][:-2]
    path = "" if path is None else path
    newline = "\n" if line[-1] == "\n" else ""
    return f"![image]({path}/{filename}){newline}"

def transform_file(source: Path, destination: Path) -> Path:
    with source.open("r") as infile, destination.open("w") as outfile:
        for line in infile:
            if is_obsidian_link(line):
                print(f"Found link in {line}")
                line = transform_link(line, "/posts/images")
            outfile.write(line)
    
    return destination

def main() -> None:
    source = Path(sys.argv[1])
    filename = source.name
    destination = Path(sys.argv[2]) / filename
    transform_file(source, destination)

if __name__ == "__main__":
    main()

