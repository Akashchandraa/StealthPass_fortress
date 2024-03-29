from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("mykey.key", "wb") as keys:
    keys.write(key)