import os
import sys

def count_lines(filepath: str):
    """Returns number of newline characters in a file"""
    with open(filepath, "r") as f:
        return f.read().count("\n")

def has_extension(filepath: str, extensions: list):
    """Returns True if filepath has any of the extensions in the
    extensions list"""
    for extension in extensions:
        if filepath.endswith(extension):
            return True
    return False

def main(path: str, extensions: list):
    """Count number of lines in all the files in a directory that has
    an extension that is in extensions list."""
    count = 0
    for path, _, files in os.walk(path):
        for filepath in files:
            if has_extension(filepath, extensions):
                count += count_lines(os.path.join(path, filepath))
    return count


if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2:]))
