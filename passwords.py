from random import sample, shuffle
import tkinter as tk
from tkinter import font as tkfont
from tkinter import simpledialog

# Define the character sets
numbers = [str(num) for num in range(2, 10)]
lower = [chr(i) for i in range(ord('a'), ord('z') + 1) if (chr(i) != 'l' and chr(i) != 'i')]
upper = [chr(i) for i in range(ord('A'), ord('Z') + 1) if (chr(i) != 'O' and chr(i) != 'I')]
puncts = ['@', '#', '$', '%', '&', '?', '*']

# Function to generate a list of passwords
def generate_passwords(num_passwords, length):
    if length < 8 or length > len(set(numbers + lower + upper + punct)):
        raise ValueError("Password length must be between 8 and the total number of unique characters available.")

    passwords = []
    for _ in range(num_passwords):
        # use sample(list, 2) where 2 will give 2 unique elements from each list
        password_chars = sample(numbers, 2) + sample(lower, 2) + sample(upper, 2) + sample(punct, 2)
        # use set() to make sure that the list only has unique elements in them
        # subtract the unique chars that we sampled from a set of all possible chars
        all_chars = list(set(numbers + lower + upper + punct) - set(password_chars))

        # use shuffle() to randomize the element in the list
        shuffle(all_chars)
        
        # length = number of chars the user wants in the password
        # - 8 because the minimum length of a password has to be 8 because we want two unique chars from each list
        # Get length - 8 chars from the end of the modified all_chars list and add that list to the original unique 8
        password_chars += all_chars[:length - 8]
        
        # shffle the list so it looks random
        shuffle(password_chars)
        
        # take the list of chars and make a string
        passwords.append(''.join(password_chars))
    return '\n'.join(passwords)

# GUI setup
root = tk.Tk()
root.withdraw()  # Hide the main window as we only need the dialog

# Ask user for input
length = simpledialog.askinteger("Input", "Enter the password length:", parent=root, minvalue=8, maxvalue=60)
num_passwords = simpledialog.askinteger("Input", "Enter the number of passwords to generate:", parent=root, minvalue=1, maxvalue=100)
user_input_spec_chars = simpledialog.askstring("Input", "Enter special characters: ", parent=root)

# if using a list of special chars from a website that specifies you can only use certain chars
# this will check if you have entered any, and if you copied and pasted the list, it will remove
# and spaces or whitespce that may be included
if user_input_spec_chars != '' :
    punct = [val for val in user_input_spec_chars if val != ' ']
else :
    punct = puncts

if length and num_passwords:  # Check if user provided both inputs
    root.deiconify()  # Show the main window again to display the passwords
    root.title("Unique Character Password Generator")

    # Generate passwords and display them
    passwords = generate_passwords(num_passwords, length)

    customFont = tkfont.Font(family="Courier new", size=20)  # Adjust font size here
    text_widget = tk.Text(root, height=num_passwords+2, width=length+4, font=customFont)
    text_widget.pack()
    text_widget.insert(tk.END, passwords)

    # Start the GUI event loop
    root.mainloop()
else:
    root.destroy()  # User cancelled input, close the application
