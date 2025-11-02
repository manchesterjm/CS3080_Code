"""
Word guessing game with web scraping functionality.

This module scrapes the top 1000 English words from a website,
stores them in an Excel file, and implements a Hangman-style word guessing game.
Users have 5 chances to guess letters in a randomly selected word.
"""

# Standard library imports
import os
from random import randint
from typing import List

# Third-party imports
import bs4
import openpyxl
import requests


# Constants
FILE_NAME = '1000_words.xlsx'
SHEET_NAME = '1000_words'

# Source URL for the 1000 words we will use
URL = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'


# Perform version check
if openpyxl.__version__ != '3.1.2':
    print("*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print("This script was made using openpyxl 3.1.2")
    print("You may experience unwanted behavior")


def check_webpage(page: str):
    """
    Fetch webpage and validate response.

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


def chk_word(letter: str, test_word: str):
    """
    Check if letter is in the word and return its indices.

    Args:
        letter: Single letter to check
        test_word: Word to check against

    Returns:
        List of indices where letter appears, or 0 if not found
    """
    word = list(test_word)
    return [indx for indx, letters in enumerate(word) if letters == letter] if letter in word else 0


def rand_cell(rows: int) -> str:
    """
    Get a random cell reference from column A.

    Args:
        rows: Maximum row number

    Returns:
        Cell reference string (e.g., 'A42')
    """
    return 'A' + str(randint(1, rows))


def get_clean_list(web_page) -> List[str]:
    """
    Extract and clean word list from webpage HTML.

    Args:
        web_page: Response object containing HTML

    Returns:
        List of cleaned words in lowercase
    """
    text_data = bs4.BeautifulSoup(web_page.text, 'html.parser')
    # Gets the 3 p tags from inside this specific div tag
    p_tags = text_data.select('div.field-item.even > p')
    word_list = p_tags[1]  # We only want the second p tag as it contains the words

    # Remove extra characters like <br> tags, newlines, tabs, and single quotes
    # Only include string elements
    return [
        elem.replace('\n\t', '').replace('\'', '').lower()
        for elem in list(word_list)
        if isinstance(elem, str)
    ]


def new_wb(lst: List[str]):
    """
    Create a new Excel workbook and save word list to active sheet.

    Args:
        lst: List of words to save

    Returns:
        Active sheet object
    """
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = SHEET_NAME

    # Fill the Excel sheet with the 1000 words from the webpage
    for i in range(1, len(lst)):
        sheet['A' + str(i)] = lst[i]
    wb.save(FILE_NAME)

    return sheet


def get_wrd(sht) -> str:
    """
    Get a random word from the workbook sheet that is at least 6 letters long.

    Args:
        sht: Excel worksheet object

    Returns:
        Random word with at least 6 letters
    """
    guess_word = []
    while len(guess_word) < 6:
        guess_word = sht[rand_cell(sht.max_row)].value
    return guess_word


def prnt_lst(lst: List[str]) -> None:
    """
    Print the list as a single joined string.

    Args:
        lst: List of strings to print
    """
    print(f"{''.join(lst)}\n")


def main():
    """Execute the main word guessing game."""
    # If an Excel spreadsheet already exists in the folder, delete to avoid problems
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    # Query webpages and get cleaned up lists of words
    cleaned_list = get_clean_list(check_webpage(URL))

    # Write list to workbook
    sheet = new_wb(cleaned_list)

    # Get a random word to guess
    guess_word = get_wrd(sheet)

    print("\nLet the game begin\n")
    print(f"Your word has {len(guess_word)} letters in it\n")

    # Fill a temp list with underscores to denote the number and positions of letters
    temp_list = ["_ " for _ in range(len(guess_word))]
    prnt_lst(temp_list)

    count = 5  # Give the user 5 misses and then terminate
    input_list = []  # Save the users inputs so we do not penalize them for duplicates

    # Use a while loop counting down to 0
    while count > 0:
        user_input = input("Please enter a letter : ")

        if user_input not in input_list:
            input_list.append(user_input)
        else:
            # No penalty for duplicate guesses
            print(f"\nYou have already tried \"{user_input}\", please try again\n")
            continue

        check = chk_word(user_input, guess_word)

        if check:
            print("You guessed a letter")

            # If there were one or more of the same letter in the word
            # add the letter in the correct index in the temp list for display
            for elem in check:
                temp_list[elem] = str(user_input) + " "
        else:
            count -= 1

            # While we still have guesses left
            if count > 0:
                print(f"Try again, you have {count} guesses left")
            else:
                # No more guesses left
                print("\nYou Lost!\n")
                break

        # Print out the current list of unknown and known letters
        prnt_lst(temp_list)

        # Check if the list has any underscores left
        # If none, then we guessed all the letters and we win
        if '_ ' not in temp_list:
            print("\nYou won!\n")
            break

    # Display word if we win or lose
    print(f"The word was \"{guess_word}\"\n\n")


if __name__ == '__main__':
    main()
