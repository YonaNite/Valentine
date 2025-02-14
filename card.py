import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Valentine's Day Card")
root.geometry("400x400")

# Create a function to handle button click
def show_message():
    messagebox.showinfo("From Kevin", "Happy Valentine's Day! 💖")

# Set the background color of the window
root.config(bg="pink")

# Add a heart symbol and message
label = tk.Label(root, text="💖 Be My Valentine 💖", font=("Brush Script MT", 24, "bold"), fg="white", bg="pink")
label.pack(pady=50)

# Add a button to show a message
button = tk.Button(root, text="Click to Open Message", command=show_message, font=("Brush Script MT", 14), bg="red", fg="white")
button.pack()

# Run the app
root.mainloop()