"""
File existence checker and remover.

This module demonstrates file creation, existence checking, and deletion
using the os module.
"""

import os


def file_exists(file: str) -> None:
    """
    Check if file exists and remove it if found.

    Args:
        file: Path to file to check and remove

    Returns:
        None
    """
    if os.path.exists(file):
        print(f"your file {file} exists")
        print(f"removing {file} now")
        os.remove(file)
    else:
        print(f"{file} not found on your computer")


def main() -> None:
    """
    Create test file, check existence, and remove.

    Returns:
        None
    """
    with open("test.txt", "w", encoding='utf-8'):
        pass  # Just create the file

    file_exists("test.txt")


if __name__ == '__main__':
    main()
