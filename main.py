"""Notes Folder Index — Build an index Markdown file from a folder of notes with titles and first lines."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='notes_folder_index',
        description='Build an index Markdown file from a folder of notes with titles and first lines.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Notes Folder Index')
    print('A table of contents for a notes directory.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
