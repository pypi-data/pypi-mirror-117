from typing import List

import typer
import nbformat
from pathlib import Path
import sys

app = typer.Typer(add_completion=False)

@app.command()
def check(root_path: str = ".", pattern = "*.ipynb"):
    root_dir = Path(root_path)

    all_errors = []
    for file in root_dir.glob(pattern):
        all_errors.extend(check_file(file))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)


def check_file(file: Path) -> List[str]:
    errors = []
    with open(file) as f:
        nb = nbformat.read(f, as_version=4)
    for idx, cell in enumerate(nb.cells, start=1):
        if cell["cell_type"] == "code":
            source_lines = cell["source"].split("\n")
            commented_lines = 0
            for line in source_lines:
                if line.strip().startswith("#"):
                    commented_lines += 1

            if commented_lines == len(source_lines):
                errors.append(f"{file} cell {idx} contains just comments")
    return errors


if __name__ == "__main__":
    app()
