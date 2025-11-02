"""
CVPR author publication analysis tool.

This module scrapes CVPR conference papers from multiple years,
identifies the top 3 authors by publication count, and generates
statistics showing their year-by-year publication counts in an Excel file.

Author: Josh Manchester
Course: CS3080
Assignment: Task 2
"""

# Standard library imports
import os
from typing import Dict, List

# Third-party imports
import bs4
import openpyxl
import requests


# Constants
FILE_NAME = 'authors.xlsx'
SHEET_NAME = 'authors'

# Source URLs - can add more or remove URLs from this list
WEBPAGE_URLS = [
    'https://openaccess.thecvf.com/CVPR2021?day=all',
    'https://openaccess.thecvf.com/CVPR2022?day=all',
    'https://openaccess.thecvf.com/CVPR2023?day=all'
]


# Perform version check
if openpyxl.__version__ != '3.1.2':
    print("*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print("This script was made using openpyxl 3.1.2")
    print("You may experience unwanted behavior")


def check_webpage(page: str):
    """
    Test that the webpage is accessible and return response.

    Args:
        page: URL of the webpage to fetch

    Returns:
        Response object from requests.get()

    Raises:
        SystemExit: If HTTP error or other error occurs
    """
    try:
        check = requests.get(page, timeout=10)
        check.raise_for_status()
        return check
    except requests.exceptions.HTTPError as http_err:
        print(f"There was an HTTP error for {page}: {http_err}")
        raise SystemExit(1) from http_err
    except Exception as err:
        print(f"There was an error accessing {page}: {err}")
        raise SystemExit(1) from err


def get_auth_pubs(auths: List[str], lst: List[str]) -> Dict[str, int]:
    """
    Get publication counts for specified authors from a list of all authors.

    Args:
        auths: List of author names to count
        lst: List of all author names from a given year

    Returns:
        Dictionary mapping author names to their publication counts
    """
    result_dict = {}
    for auth in auths:
        counter = 0
        for name in lst:
            if name == auth:
                counter += 1
        result_dict[auth] = counter
    return result_dict


def get_clean_list(web_page) -> List[str]:
    """
    Extract and clean author names from webpage HTML.

    Args:
        web_page: Response object containing HTML

    Returns:
        List of author names
    """
    text_data = bs4.BeautifulSoup(web_page.text, 'html.parser')
    tags_lst = text_data.select('input[name="query_author"]')
    return [tag.get('value') for tag in tags_lst]


def get_top_auths(lst: List[str]) -> List[str]:
    """
    Identify the top three authors by total publication count.

    Args:
        lst: List of all author names across all years

    Returns:
        List of the top 3 author names
    """
    author_counts = {}
    for auth in lst:
        if auth in author_counts:
            author_counts[auth] += 1
        else:
            author_counts[auth] = 1

    # Use lambda function to sort by count in descending order
    # Grab the top three entries
    top_auths = sorted(author_counts.items(), key=lambda item: item[1], reverse=True)[:3]
    return [name for name, _ in top_auths]


def new_wb(data: Dict[str, Dict[str, int]]) -> int:
    """
    Create Excel workbook with author publication data.

    Creates a spreadsheet with years as rows, authors as columns,
    and includes a totals row at the bottom.

    Args:
        data: Nested dictionary with structure {year: {author: count}}

    Returns:
        0 on success
    """
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = SHEET_NAME

    years = list(data.keys())
    # Get unique list of authors from the nested dictionary
    authors = list(set(auth for year in data for auth in data[year]))

    # Create the header row with author names
    sheet.append([''] + authors)

    # Create one row for each year with publication counts per author
    for year in years:
        sheet.append([year] + [data[year].get(author, 0) for author in authors])

    # Create the totals row
    totals_row = ['Totals']
    for author in authors:
        totals_row.append(sum(data[year].get(author, 0) for year in years))
    sheet.append(totals_row)

    wb.save(FILE_NAME)
    return 0


def main():
    """Execute the main author analysis workflow."""
    # If an Excel spreadsheet already exists, delete to avoid problems
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    # Query webpages and get cleaned up lists of authors
    clean_lists = [get_clean_list(check_webpage(url)) for url in WEBPAGE_URLS]

    # Make a combined list of all cleaned up lists
    cleaned_all = sum(clean_lists, [])

    # Get a list of top authors for all years
    top_auths = get_top_auths(cleaned_all)

    # Extract years from URLs (split at CVPR, then at ?)
    years = [url.split('CVPR')[1].split('?')[0] for url in WEBPAGE_URLS]

    # Get the top authors' number of publications for each year
    dict_all = {}
    for lst, year in zip(clean_lists, years):
        dict_all[year] = get_auth_pubs(top_auths, lst)

    # Make a workbook with the top authors and publication counts per year
    new_wb(dict_all)

    print(f"Analysis complete. Results saved to {FILE_NAME}")


if __name__ == '__main__':
    main()
