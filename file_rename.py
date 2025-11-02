"""
File renaming utility based on modification timestamps.

This module renames files in a directory based on their last modified timestamp,
creating a standardized naming convention of YYYY-MM-DD_HH-MM-SS.
"""

import os
import re
from datetime import datetime


# Directory containing files to rename
DIRECTORY = r'D:\Pictures\Wallpapers'

# Pattern to match existing datetime format in filenames
DATETIME_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}')


def rename_files_by_timestamp(directory: str) -> tuple[int, dict[str, int]]:
    """
    Rename files in directory based on their modification timestamp.

    Args:
        directory: Path to directory containing files to rename

    Returns:
        tuple: (total_files, date_count_dict) where date_count_dict maps
               dates to number of files modified on that date

    Example:
        >>> total, counts = rename_files_by_timestamp(r'C:\\Pictures')
        >>> print(f"Processed {total} files")
    """
    date_count = {}
    total_files = 0

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        total_files += 1

        # Get the full file path
        old_file = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(old_file):
            continue

        # Get the last modified time of the file
        mod_time = os.path.getmtime(old_file)

        # Convert it to a datetime object
        date_time = datetime.fromtimestamp(mod_time)

        # Extract just the date part
        date_key = date_time.strftime('%Y-%m-%d')

        # Increment the count for this date
        if date_key in date_count:
            date_count[date_key] += 1
        else:
            date_count[date_key] = 1

        # Check if the filename already matches the datetime pattern
        if DATETIME_PATTERN.match(filename):
            continue

        # Format the datetime object as a string in the desired format
        new_filename = date_time.strftime('%Y-%m-%d_%H-%M-%S')

        # Generate new file path with the same extension as the original file
        file_extension = os.path.splitext(filename)[1]
        new_file = os.path.join(directory, new_filename + file_extension)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed "{old_file}" to "{new_file}"')

    return total_files, date_count


def main() -> None:
    """
    Execute file renaming process and display statistics.

    Returns:
        None
    """
    total_files, date_count = rename_files_by_timestamp(DIRECTORY)

    # Output the results
    print(f'Total number of files in the directory: {total_files}')
    print("Files downloaded per day:")
    for date, count in sorted(date_count.items()):
        print(f"{date}: {count} files")


if __name__ == '__main__':
    main()
