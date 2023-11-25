#!/usr/bin/env python

from pathlib import Path

def main() -> None:

    path = Path('.')

    for filepath in path.iterdir():

        if filepath.is_dir():
            continue

        topdir = Path(f"./Movies-{filepath.name[0]}")
        topdir.mkdir(exist_ok=True)

        new_filepath = topdir / filepath

        filepath.rename(new_filepath)

        

if __name__ == '__main__':
    main()
