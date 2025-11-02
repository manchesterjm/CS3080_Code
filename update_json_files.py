"""
JSON field renamer utility.

This module processes JSON files in a directory and replaces a specific
field name within the "result" block from "item" to "id".
"""

import glob
import json
import os


def replace_text_in_files(directory: str) -> None:
    """
    Replace 'item' field with 'id' in JSON result blocks.

    Processes all .json files in the specified directory and renames
    the "item" field to "id" within the "result" block if present.

    Args:
        directory: Path to directory containing JSON files to process

    Returns:
        None

    Example:
        >>> replace_text_in_files(r'C:\\json_files')
    """
    # Get all .json files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # Loop through each file
    for file_path in json_files:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Check if the "result" block contains "item" and replace it with "id"
        if 'result' in data and 'item' in data['result']:
            data['result']['id'] = data['result'].pop('item')

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Processed file: {file_path}")


def main() -> None:
    """
    Execute JSON field replacement on specified directory.

    Returns:
        None
    """
    # Specify the directory containing the .json files
    directory = (
        r'd:\Downloads\VanillaTweaks_c419099_MC1.20-1.20.4'
        r'\data\slabs_stairs_to_block\recipes\stairs'
    )

    replace_text_in_files(directory)


if __name__ == '__main__':
    main()
