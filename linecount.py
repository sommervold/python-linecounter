import os
import sys
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


def main(path: str, extensions: list[str], ignore: list[str]):
    """Count number of lines in all the files in a directory that has
    an extension that is in extensions list."""
    count = 0
    for path, _, files in os.walk(path):
        for filepath in files:
            if has_extension(filepath, extensions):
                count += count_lines(os.path.join(path, filepath))
    return count


class _LinecountNamespace(argparse.Namespace):
    path: str
    exclude: list[str]
    extensions: list[str]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        default=".",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        default=[],
        help="Files and directories with this name will be ignored.",
    )
    parser.add_argument(
        "-e",
        "--extension",
        action="append",
        default=[],
        help="Files with this extension will be included in the count.",
    )

    args: _LinecountNamespace = parser.parse_args()
    result = main(args.path, args.extensions, args.exclude)
