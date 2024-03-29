from cryptography.fernet import Fernet

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

#print(key)
def encryption():
    f = Fernet(key)

    with open("__pycache__\\notes.txt", "rb") as file:
        files = file.read()

    encrypted = f.encrypt(files)
    with open("registered_users\\user_infomation.txt", "wb") as encrypt_file:
        encrypt_file.write(encrypted)
encryption()