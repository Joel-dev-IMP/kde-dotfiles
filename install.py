#!/usr/bin/env python3

from pathlib import Path
from globals import TEXT_FILES, BINARY_FILES, TARGET_PATH, SOURCE_PATH


def replace_variables(input: str) -> str:
    return input.replace("KDE_DOT_EXPANDUSER", str(Path("~").expanduser()))


def main() -> None:
    for src in TEXT_FILES:
        target = TARGET_PATH / src.relative_to(SOURCE_PATH)
        target.parent.mkdir(exist_ok=True)

        with src.open("r") as f:
            data: str = replace_variables(f.read())

        with target.open("w+") as f:
            f.write(data)

        if target.stem == ".sh":
            target.chmod(0o755)

    for src in BINARY_FILES:
        target = TARGET_PATH / src.relative_to(SOURCE_PATH)
        target.parent.mkdir(exist_ok=True)

        src.copy(target)


if __name__ == "__main__":
    main()
