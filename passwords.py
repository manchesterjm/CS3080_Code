"""
Unique character password generator with GUI.

This module generates secure passwords with guaranteed character diversity
(numbers, lowercase, uppercase, special characters) and displays them in a GUI.
"""

from random import sample, shuffle
import tkinter as tk
from tkinter import font as tkfont, simpledialog


# Default character sets
NUMBERS = [str(num) for num in range(2, 10)]
LOWER = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in ('l', 'i')]
UPPER = [chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) not in ('O', 'I')]
PUNCTS = ['@', '#', '$', '%', '&', '?', '*']


def generate_passwords(num_passwords: int, length: int, punct: list[str]) -> str:
    """
    Generate a list of unique character passwords.

    Each password contains at least 2 characters from each category:
    numbers, lowercase, uppercase, and special characters.

    Args:
        num_passwords: Number of passwords to generate
        length: Length of each password (minimum 8)
        punct: List of special characters to use

    Returns:
        str: Newline-separated string of generated passwords

    Raises:
        ValueError: If length is less than 8 or exceeds available unique characters

    Example:
        >>> passwords = generate_passwords(5, 12, PUNCTS)
        >>> print(passwords)
    """
    if length < 8 or length > len(set(NUMBERS + LOWER + UPPER + punct)):
        raise ValueError(
            "Password length must be between 8 and the total number of unique characters available."
        )

    passwords = []
    for _ in range(num_passwords):
        # Use sample(list, 2) to get 2 unique elements from each list
        password_chars = sample(NUMBERS, 2) + sample(LOWER, 2) + sample(UPPER, 2) + sample(punct, 2)
        # Subtract the unique chars that we sampled from a set of all possible chars
        all_chars = list(set(NUMBERS + LOWER + UPPER + punct) - set(password_chars))

        # Randomize the element order in the list
        shuffle(all_chars)

        # Get remaining characters to reach desired length
        password_chars += all_chars[:length - 8]

        # Shuffle the list so it looks random
        shuffle(password_chars)

        # Take the list of chars and make a string
        passwords.append(''.join(password_chars))
    return '\n'.join(passwords)


def main() -> None:
    """
    Run password generator GUI and display generated passwords.

    Returns:
        None
    """
    # GUI setup
    root = tk.Tk()
    root.withdraw()  # Hide the main window as we only need the dialog

    # Ask user for input
    length = simpledialog.askinteger(
        "Input",
        "Enter the password length:",
        parent=root,
        minvalue=8,
        maxvalue=60
    )
    num_passwords = simpledialog.askinteger(
        "Input",
        "Enter the number of passwords to generate:",
        parent=root,
        minvalue=1,
        maxvalue=100
    )
    user_input_spec_chars = simpledialog.askstring(
        "Input", "Enter special characters: ", parent=root
    )

    # Process special characters input
    # Remove any spaces or whitespace that may be included
    if user_input_spec_chars != '':
        punct = [val for val in user_input_spec_chars if val != ' ']
    else:
        punct = PUNCTS

    if length and num_passwords:  # Check if user provided both inputs
        root.deiconify()  # Show the main window again to display the passwords
        root.title("Unique Character Password Generator")

        # Generate passwords and display them
        passwords = generate_passwords(num_passwords, length, punct)

        custom_font = tkfont.Font(family="Courier new", size=20)
        text_widget = tk.Text(root, height=num_passwords+2, width=length+4, font=custom_font)
        text_widget.pack()
        text_widget.insert(tk.END, passwords)

        # Start the GUI event loop
        root.mainloop()
    else:
        root.destroy()  # User cancelled input, close the application


if __name__ == '__main__':
    main()
