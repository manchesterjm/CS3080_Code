"""
MP3 file reordering utility for legacy MP3 players.

This module physically reorders MP3 files on a USB drive by rewriting
directory entries in alphabetical order for older MP3 players that read
track order from FAT directory entry order.
"""

import os
import shutil


def reorder_mp3_files(usb_path: str) -> None:
    """
    Reorder MP3 files alphabetically by rewriting directory entries.

    This function helps older MP3 players that read track order from
    the FAT directory entry order rather than by filename. It creates
    a temporary folder, moves files in sorted order, and moves them back
    to force new directory entries.

    Args:
        usb_path: Path to USB drive containing MP3 files

    Returns:
        None

    Example:
        >>> reorder_mp3_files(r'G:\\')
    """
    # Get all MP3 files (case-insensitive for .mp3)
    mp3_files = [f for f in os.listdir(usb_path) if f.lower().endswith('.mp3')]

    # Sort them by name
    mp3_files.sort()

    # Create a temporary folder to force new directory entries
    temp_folder = os.path.join(usb_path, "temp_reorder")
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    # Move the MP3s into the temp folder in alphabetical order
    # WITHOUT changing the filenames
    for filename in mp3_files:
        old_path = os.path.join(usb_path, filename)
        new_path = os.path.join(temp_folder, filename)
        shutil.move(old_path, new_path)

    # Move the MP3s back to the root (usb_path) in alphabetical order
    # so the final directory entries are re-created in sorted order
    reordered_files = sorted(os.listdir(temp_folder))
    for filename in reordered_files:
        old_path = os.path.join(temp_folder, filename)
        new_path = os.path.join(usb_path, filename)
        shutil.move(old_path, new_path)

    # Remove the temp folder
    os.rmdir(temp_folder)


def main() -> None:
    """
    Execute MP3 file reordering on USB drive.

    Returns:
        None
    """
    usb_drive_path = r"G:\\"

    reorder_mp3_files(usb_drive_path)
    print("Reordering complete. Safely eject the USB drive and test in your MP3 player.")


if __name__ == '__main__':
    main()
