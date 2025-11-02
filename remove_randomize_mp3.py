"""
MP3 filename prefix remover.

This module removes three-digit number prefixes from MP3 filenames
that follow the pattern "nnn - filename.mp3".
"""

import os
import re


def rename_files(directory: str) -> None:
    """
    Remove three-digit number prefix from MP3 filenames.

    Renames files that start with "nnn - " where 'nnn' is a three-digit integer
    by removing the first 6 characters (including the space and dash).

    Args:
        directory: The directory path to process

    Returns:
        None

    Example:
        >>> rename_files(r'G:\\')
    """
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            if re.match(r"^\d{3} - ", filename):
                new_filename = filename[6:]  # Remove first 6 characters
                new_filepath = os.path.join(directory, new_filename)
                os.rename(filepath, new_filepath)


def main() -> None:
    """
    Execute MP3 filename prefix removal on USB drive.

    Returns:
        None
    """
    directory_path = r"G:\\"
    rename_files(directory_path)


if __name__ == '__main__':
    main()
