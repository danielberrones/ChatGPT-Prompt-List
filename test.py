import tkinter as tk
from tkinter import messagebox
import random

def generate_random_number():
    """Generate a random number and display it in a Tkinter messagebox."""
    random_number = random.randint(1, 1000)
    messagebox.showinfo("Random Number", f"The random number is: {random_number}")

def create_tkinter_window():
    """Create a Tkinter window with a button."""
    window = tk.Tk()
    window.title("Random Number Generator")

    # Create a button widget
    button = tk.Button(window, text="Generate Random Number", command=generate_random_number)
    button.pack(pady=10)

    window.mainloop()

# Call the function to create the Tkinter window
create_tkinter_window()
