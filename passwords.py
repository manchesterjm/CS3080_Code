from random import sample, shuffle
import tkinter as tk
from tkinter import font as tkfont
from tkinter import simpledialog

# Define the character sets
numbers = [str(num) for num in range(0, 10)]
lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
puncts = ['@', '#', '$', '%', '&']

# Function to generate a list of passwords
def generate_passwords(num_passwords, length):
    if length < 8 or length > len(set(numbers + lower + upper + punct)):
        raise ValueError("Password length must be between 8 and the total number of unique characters available.")

    passwords = []
    for _ in range(num_passwords):
        password_chars = sample(numbers, 2) + sample(lower, 2) + sample(upper, 2) + sample(punct, 2)
        all_chars = list(set(numbers + lower + upper + punct) - set(password_chars))
        shuffle(all_chars)
        password_chars += all_chars[:length - 8]
        shuffle(password_chars)
        passwords.append(''.join(password_chars))
    return '\n'.join(passwords)

# GUI setup
root = tk.Tk()
root.withdraw()  # Hide the main window as we only need the dialog

# Ask user for input
length = simpledialog.askinteger("Input", "Enter the password length:", parent=root, minvalue=8, maxvalue=60)
num_passwords = simpledialog.askinteger("Input", "Enter the number of passwords to generate:", parent=root, minvalue=1, maxvalue=100)
spec_chars = simpledialog.askstring("Input", "Enter special characters: ", parent=root)
if spec_chars != '' :
    punct = [val for val in spec_chars if val != ' ']
else :
    punct = puncts

if length and num_passwords:  # Check if user provided both inputs
    root.deiconify()  # Show the main window again to display the passwords
    root.title("Unique Character Password Generator")

    # Generate passwords and display them
    passwords = generate_passwords(num_passwords, length)

    customFont = tkfont.Font(family="Courier new", size=20)  # Adjust font size here
    text_widget = tk.Text(root, height=15, width=50, font=customFont)
    text_widget.pack()
    text_widget.insert(tk.END, passwords)

    # Start the GUI event loop
    root.mainloop()
else:
    root.destroy()  # User cancelled input, close the application
