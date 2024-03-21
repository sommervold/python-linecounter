#!/usr/bin/python

import os
import argparse


def count_lines(filepath: str):
    """Returns number of newline characters in a file"""
    try:
        with open(filepath, "r") as f:
            return f.read().count("\n")
    except UnicodeDecodeError as e:
        # Likely a binary file, skip.
        return 0


def has_extension(filepath: str, extensions: list[str]):
    """Returns True if filepath has any of the extensions in the
    extensions list"""
    for extension in extensions:
        if filepath.endswith(extension):
            return True
    return False


def main(paths: list[str], extensions: list[str], ignore: list[str]):
    """Count number of lines in all the files in a directory that has
    an extension that is in extensions list."""
    count = 0
    for path in paths:
        for path, dirnames, files in os.walk(path, topdown=True):

            # os.walk will only search directories present in dirnames.
            for dir in ignore:
                if dir in dirnames:
                    dirnames.remove(dir)

            if os.path.basename(path) in ignore:
                continue
            for filepath in files:
                if has_extension(filepath, extensions):
                    count += count_lines(os.path.join(path, filepath))
    return count


class _LinecountNamespace(argparse.Namespace):
    path: list[str]
    ignore: list[str]
    extension: list[str]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        action="append",
        default=[],
        help="Directories that should be searched"
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        default=[],
        help="Directories with this name will be ignored.",
    )
    parser.add_argument(
        "-e",
        "--extension",
        action="append",
        default=[],
        help="Files with this extension will be included in the count.",
    )
    args: _LinecountNamespace = parser.parse_args()
    result = main(args.path, args.extension, args.ignore)
    print(result)
