import os
import re
import time
import tkinter as tk
import winsound as wn
from tkinter import PhotoImage, messagebox, simpledialog

import cv2
import numpy as np
import pyfiglet
import pyttsx3
from ffpyplayer.player import MediaPlayer
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play

from email_credentials import email, password
from enfile import encryption
from send_email import send_emails

# Initializing the required variables
start = time.time()
password_attempts = 0
max_attempts = 3
warning = pyttsx3.init()
image_count = 0  # Initialize image_count
save_path_users = 'registered_users'
os.makedirs(save_path_users, exist_ok=True)
email_from = email
email_list = ["akashchandraambula@gmail.com", email]
# Function to record and store the face of a thief
save_path = 'pictures of unauthorized persons'
os.makedirs(save_path, exist_ok=True)

existing_images = [f for f in os.listdir(save_path) if f.endswith('.png')]
numeric_parts = [int(re.search(r'\d+', f).group()) for f in existing_images if re.search(r'\d+', f)]
highest_count = max(numeric_parts, default=0)

# Global variable for image count
image_count = highest_count
def check_password_strength(password):
    """
    Check the strength of a password based on various criteria.
    Returns a tuple (strength, feedback_message).
    """
    # Minimum length requirement
    min_length = 8

    if len(password) < min_length:
        return 0, f"Password should be at least {min_length} characters long."

    # Check for the presence of uppercase letters
    if not any(char.isupper() for char in password):
        return 1, "Include at least one uppercase letter for better security."

    # Check for the presence of lowercase letters
    if not any(char.islower() for char in password):
        return 1, "Include at least one lowercase letter for better security."

    # Check for the presence of numbers
    if not any(char.isdigit() for char in password):
        return 1, "Include at least one number for better security."

    # Check for the presence of special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        return 1, f"Include at least one special character ({special_characters}) for better security."

    return 2, "Strong password! You can use this."

# Function to register a new user
def register_user():
    global image_count
    
    first_name = simpledialog.askstring("User Registration", "First_Name:",parent=root)
    if first_name is None or first_name.strip() == "":
        root.destroy()
        return None, None
    last_name = simpledialog.askstring("User Registration", "Last_Name:",parent=root)
    if last_name is None or last_name.strip() == "":
        root.destroy()
        return None, None
    Branch = simpledialog.askstring("User Registration", "Branch:",parent=root)
    if Branch is None or Branch.strip() == "":
        root.destroy()
        return None, None
    Roll_number = simpledialog.askstring("User Registration","Roll_number:",parent=root)
    if Roll_number is None or Roll_number.strip() == "":
        root.destroy()
        return None, None
    clg_gmail_id = simpledialog.askstring("User Registration", "Clg_gmail_id:",parent=root)
    if clg_gmail_id is None or clg_gmail_id.strip() == "":
        root.destroy()
        return None, None
    password = None

    while True:
        password = simpledialog.askstring("User Registration", "password:", show="👻",parent=root)
        if password is None or password.strip() == "":
            root.destroy()
            return None, None
        strength, feedback = check_password_strength(password)
        messagebox.showinfo("Password Strength", feedback)
        if strength == 2:
            break


    user_directory = os.path.join("registered_users\\photos", Roll_number)
    
    #Check if the first_name already exists
    if os.path.exists(user_directory):
        messagebox.showerror("User Registration", "Roll_number already exists.")
        register_user()
        return
    

    #Create a directory for the user
    os.makedirs(user_directory)

    image_capture = cv2.VideoCapture(0)
    if not image_capture.isOpened():
        print(f"Error: Could not open external webcam at index {2}.")
        exit()
    _, frame = image_capture.read()
    image_count += 1
    image_name = f'{first_name}_{image_count}.png'
    image_path = os.path.join(user_directory, image_name)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(image_path, frame_rgb)
    image_capture.release()

    with open('__pycache__\\notes.txt', 'a') as file:
        file.write(f'first_name = {first_name}\nLast_name = {last_name}\nBranch = {Branch}\nRoll_Number = {Roll_number}\ncollege email_id = {clg_gmail_id}\nPassword = {password}\n\n')

    messagebox.showinfo("User Registration", "Registration successful. You can now log in.")
    show_custom_message("queries","If you have any queries regarding this product, please contact:\nakashchandraambula@gmail.com")
    encryption()

def play_video():

    video_path = "files\\video.mp4"
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("select the correct video path")
        exit()
    player = MediaPlayer(video_path)
    while True:
        ret, frame = video_capture.read()
        audio_framem, val = player.get_frame()
        if not ret:
            break
        cv2.imshow("video", frame)
        if cv2.waitKey(25) & 0xFF == ord('b'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


def capture_face():
    global image_count
    image_capture = cv2.VideoCapture(0)
    _, frame = image_capture.read()
    image_capture.release()
    image_count += 1
    image_name = f'captured_image_{image_count}.png'
    image_path = os.path.join(save_path, image_name)
    cv2.imwrite(image_path, frame)

def warn():
    warning.say("Leave my device, you are already captured..")
    print(pyfiglet.figlet_format("LOGIN UNSUCCESSFUL😡😤"))

    warning.runAndWait()

def show_custom_message(title, message):
    messagebox.showinfo(title, message)

def login_attempt():
    global password_attempts
    username = simpledialog.askstring("Login👻", "Enter your username:👻🫡", parent=root)
    if username is None or username.strip() == "":
        root.destroy()
        return None, None
    password = simpledialog.askstring("Login👻", "Enter password:👻🫡", parent=root, show='*')
    if password is None or password.strip() == "":
        root.destroy()
        return None, None
    if password == "akash123" and username == "akash":
        warning.say("Good job Akaash, you are successfully logged into your device.")
        warning.runAndWait()
        print(pyfiglet.figlet_format("Login Successfull"))

        show_custom_message("Login Successful😎😉😎\n",
                            "Akaash, you have successfully logged in please go through the registration page.👍🥳🥳")
        response = messagebox.askyesno("User Registration", "Do you want to register a user details?")
        if response:
            register_user()
        
        

        return True
    else:
        warning.say("Akaash, please kindly enter your correct credentials.")
        warning.runAndWait()
        password_attempts += 1

        if password_attempts == max_attempts:
            
            capture_face()
            #warn()
            play_video()
            show_custom_message("Account Locked!😓",
                                "Too many unsuccessful login attempts. Your account has been locked for security reasons.")
            send_emails(email_list)
            return False
        else:
            show_custom_message("Login Failed🥲🙂🫡",
                                f"wrong first_name or password 😡😡😡\nmake sure you entered the correct credentials!🙌👍🙌\n Attempts left: {max_attempts - password_attempts}")
            return False

def main():
    global root
    root = tk.Tk()
    root.title("Stealthpass fortress")
    root.geometry("800x600")

    bg_image_path = "files\\bg6.jpg"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((1000, 800))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    capture_button = tk.Button(root, text="", command=capture_face, bg="cyan", fg="black")
    capture_button.place(relx=0.5, rely=0.8, anchor="center")

    #print(pyfiglet.figlet_format("Enter your password🫡"))
    print("system was runing")

    while password_attempts < max_attempts:
        result = login_attempt()

        if result:
            break

#    response = messagebox.askyesno("User Registration", "Do you want to register as a new user?")
#    if response:
#        register_user()
    
    print("system closed \nThank you")
    print("If you have any queries regarding this product, please contact:")
    print("akashchandraambula@gmail.com")

if __name__ == "__main__":
    main()
