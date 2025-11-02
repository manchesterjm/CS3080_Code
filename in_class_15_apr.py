"""
Excel to JSON converter.

This module reads data from an Excel file and converts it to JSON format,
both printing the JSON string and writing it to a file.
"""

import json

import openpyxl


def main() -> None:
    """
    Convert Excel data to JSON format.

    Reads a range of cells from an Excel file, converts them to a dictionary,
    and saves the result as a JSON file.

    Returns:
        None
    """
    wb = openpyxl.load_workbook('two.xlsx')
    sheet = wb.active

    items = sheet['A2':'B6']

    # Convert to dictionary
    dict_nums = {}
    for rows in items:
        key = rows[0].value
        value = rows[1].value
        dict_nums[key] = value

    print(dict_nums)

    json_dump = json.dumps(dict_nums)

    print(json_dump)

    with open('test.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict_nums, json_file)


if __name__ == '__main__':
    main()
