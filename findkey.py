import pyperclip
import tkinter as tk
from tkinter import simpledialog, messagebox

def copy_to_clipboard(key):
    pyperclip.copy(key)

def your_key():
    password = simpledialog.askstring("Login", "Enter password:", show='*')
    if password is None or password.strip() == "":
        messagebox.showerror(title="Error!", message="Password cannot be empty.")
        return False
    elif password == "akash123":
        try:
            with open("mykey.key", "rb") as mykey:
                key = mykey.read().decode('utf-8')
        except FileNotFoundError:
            messagebox.showerror(title="Error!", message="Key file not found.")
            return False

        copy_to_clipboard(key)
        messagebox.showinfo("Success", "Key has been copied to the clipboard.")
        return True
    else:
        messagebox.showerror("Error", "Incorrect password.")
        return False

if __name__ == '__main__':
    your_key()