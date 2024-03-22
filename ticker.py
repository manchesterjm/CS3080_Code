import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get current time in seconds since the epoch
    time_display.config(text=str(current_time))
    root.after(200, update_time)  # Schedule the update_time function to be called after 1000ms

root = tk.Tk()
root.title("Time in Seconds")

time_display = tk.Label(root, font=('Arial', 48))
time_display.pack()

update_time()  # Initial call to display the time and start the updates

root.mainloop()