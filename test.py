import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Valentine's Day Card")
root.geometry("500x500")

# List of cheesy pickup lines
pickup_lines = [
    "Are you French? Cuz Eiffel for you!",
    "Do you have a Band-Aid? Cuz I just scraped my knee falling for you!",
    "Are you a magician? Cuz whenever I look at you, everyone else disappears!",
    "Are you a parking ticket? Cuz you've got 'FINE' written all over you!",
    "Do you have a map? I keep getting lost in your eyes!",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Are you a campfire? Cuz you're hot and I want s'more!",
    "If beauty were a crime, you'd be serving a life sentence!",
    "Are you a Wi-Fi signal? Cuz I'm feeling a connection!",
    "Are you a loan? Cuz you've got my interest",
    "Are you a camera? Cuz all I can do is smile when I see you",
    "Are you a parking ticket? Cuz you've got 'FINE' written all over you!",
    "Are you a time traveler? Cuz I can see you in my future!",
    "Is your name Google? Cuz you have everything I've been searching for! ",
    "Are you made of copper and tellurium? Because you're Cu-Te!",
    "Did the sun come out, or did you just smile at me?",
    "I'd give up my morning cereal to spoon you instead.",
    "I love my bed, but I'd rather be in yours.",
    "It's a good thing I have my library card, because I am totally checking you out.",
    "If I could rearrange the alphabet, I'd put U and I together.",
    "Anyone who says Disneyland is the happiest place on earth has clearly never stood next to you.",
    "If you were words on a page you'd be the fine print.",
    "You know those gaps between your fingers? I think they were made for mine.",
    "Want to grab coffee? I like you a latte."

]

# Create a function to handle button click
def show_message():
    # Choose a random pickup line from the list
    message = random.choice(pickup_lines)
    messagebox.showinfo("Cheesy Pickup Line", message)

# Set the background color of the window to a soft pastel
root.config(bg="#FFB0E1")  # Light pink background

# Add a cute heart symbol and message with a cursive font
label = tk.Label(root, text="💖 Be My Valentine 💖", font=("Brush Script MT", 28, "bold"), fg="#BFE8FF", bg="#FFB0E1")
label.pack(pady=40)


# Cute Button
def on_enter(e):
    button.config(bg="#9ECF99")  # Different color on hover

def on_leave(e):
    button.config(bg="#FF69B4")  # Back to original color

button = tk.Button(root, text="💘 Click to Open Message 💘", command=show_message, 
                   font=("Brush Script MT", 16), fg="white", bg="#D5C2FF", 
                   relief="flat", padx=20, pady=10, bd=10, cursor="hand2")
button.pack(pady=20)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
# Optional: Add some cute little hearts or icons as a border
heart_label = tk.Label(root, text="💖💖💖", font=("Comic Sans MS", 24), fg="#BFE8FF", bg="#FFB0E1")
heart_label.pack(pady=10)

# Run the app
root.mainloop()