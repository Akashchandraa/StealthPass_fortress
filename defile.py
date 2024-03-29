from cryptography.fernet import Fernet, InvalidToken
import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import base64
import binascii

key = simpledialog.askstring(title="Enter Key", prompt="Please enter the key:")

try:
    # Try to decode the key to ensure it is a valid base64-encoded key
    key_bytes = base64.urlsafe_b64decode(key)
    assert len(key_bytes) == 32
except (binascii.Error, AssertionError):
    messagebox.showerror(title="Invalid Key", message="You passed an invalid key. Please make sure the key is correct.")
    exit()

f = Fernet(key)

with open("registered_users\\user_infomation.txt", "rb") as file:
    files = file.read()

try:
    decrypted = f.decrypt(files)
except InvalidToken:
    messagebox.showerror(title="Decryption Error", message="Invalid key for decryption. Please make sure the key is correct.")
    print("Invalid key for decryption. Please make sure the key is correct.")


with open("registered_users\\user_infomation(decrypted_file).txt", "wb") as dencrypt_file:
    dencrypt_file.write(decrypted)

messagebox.showinfo(title="Decryption Successful!", message="The user information has been decrypted successfully.")
print("The user information has been decrypted successfully.")