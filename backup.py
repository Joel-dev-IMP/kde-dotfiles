#!/usr/bin/env python3

from pathlib import Path
from globals import TEXT_FILES, BINARY_FILES, TARGET_PATH, SOURCE_PATH, KITTY_FILES


def replace_variables(input: str) -> str:
    return input.replace(str(Path("~").expanduser()), "KDE_DOT_EXPANDUSER")


def main() -> None:
    for target in TEXT_FILES:
        src = TARGET_PATH / target.relative_to(SOURCE_PATH)

        with src.open("r") as f:
            data: str = replace_variables(f.read())

        with target.open("w+") as f:
            f.write(data)

    for target in BINARY_FILES:
        src = TARGET_PATH / target.relative_to(SOURCE_PATH)

        src.copy(target)

    for target in KITTY_FILES:
        src = TARGET_PATH / target.relative_to(SOURCE_PATH)

        src.copy(target)


if __name__ == "__main__":
    main()
