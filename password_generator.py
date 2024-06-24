import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_special, use_numbers):
    characters = string.ascii_lowercase  # always include lowercase letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_password_and_update_label():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return
        
        use_uppercase = uppercase_var.get()
        use_special = special_var.get()
        use_numbers = numbers_var.get()
        
        password = generate_password(length, use_uppercase, use_special, use_numbers)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Variables to track user choices
uppercase_var = tk.BooleanVar()
special_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()

# Create and pack GUI elements
label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_and_update_label)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
