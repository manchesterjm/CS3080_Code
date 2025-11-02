"""
MP3 file randomizer with sequential numbering.

This module randomizes the order of MP3 files in a directory and adds
sequential three-digit number prefixes for proper playback ordering.
"""

import os
import random


def randomize_and_rename_files(source_directory: str) -> None:
    """
    Randomize MP3 files order and add three-digit number prefix.

    Args:
        source_directory: Path to the directory containing the MP3 files

    Returns:
        None

    Raises:
        Exception: If file operations fail

    Example:
        >>> randomize_and_rename_files(r'G:\\')
    """
    try:
        # Get a list of all MP3 files in the directory
        mp3_files = [f for f in os.listdir(source_directory) if f.endswith('.mp3')]

        # Shuffle the list randomly
        random.shuffle(mp3_files)

        # Create a counter for the three-digit prefix
        counter = 1

        # Rename each file with the prefix and new order
        for file in mp3_files:
            new_name = f"{str(counter).zfill(3)} - {file}"
            os.rename(
                os.path.join(source_directory, file),
                os.path.join(source_directory, new_name)
            )
            counter += 1

        print(f"Successfully randomized and renamed {len(mp3_files)} files in {source_directory}")

    except (OSError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")


def main() -> None:
    """
    Execute MP3 file randomization on USB drive.

    Returns:
        None
    """
    # Replace with the actual path to your USB drive
    usb_drive_path = r"G:\\"

    randomize_and_rename_files(usb_drive_path)


if __name__ == '__main__':
    main()
