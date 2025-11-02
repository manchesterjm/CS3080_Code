"""
Excel workbook sheet name display.

This module loads an Excel workbook and displays the names of all sheets.
"""

import openpyxl


def main() -> None:
    """
    Load Excel file and display sheet names.

    Returns:
        None
    """
    wb_one = openpyxl.load_workbook('test.xlsx')
    print(wb_one.sheetnames)


if __name__ == '__main__':
    main()
