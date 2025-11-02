"""
Real-time clock display using Tkinter.

This module creates a GUI window displaying the current time updated
every 200 milliseconds.
"""

import time
import tkinter as tk


def update_time(time_display: tk.Label, root: tk.Tk) -> None:
    """
    Update time display and schedule next update.

    Args:
        time_display: Label widget to update with current time
        root: Root Tkinter window

    Returns:
        None
    """
    current_time = time.strftime("%H:%M:%S")
    time_display.config(text=str(current_time))
    root.after(200, lambda: update_time(time_display, root))


def main() -> None:
    """
    Create and run time display GUI.

    Returns:
        None
    """
    root = tk.Tk()
    root.title("Time in Seconds")

    time_display = tk.Label(root, font=('Arial', 48))
    time_display.pack()

    update_time(time_display, root)

    root.mainloop()


if __name__ == '__main__':
    main()
