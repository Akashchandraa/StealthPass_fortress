inbuild modules/libraries
1) OS
2) RE
3) TIME
4) TKINTER
5) WINSOUND
6) CV2
7) PYFIGLET
8) PYTTSX3
9) PIL (pillow)
10) CRYPTOGRAPHY 
11) SMTP
12) TWILO
13) EMAIL

my modules/user build modules
1) ENFILE
2) EMAIL_CREDENTIALS
3) SEND_EMAIL

HOW SYSTEM WORKS:
Base concept:
Our system’s first page is a kind of login page where the authorized person or an administrator has to enter the required credentials to login. After login they can able to see a user registration page where they can enter the details of the new user after entering the details the system automatically takes the picture of the new user and stores them in the local database.
Security or core concept:

1)Monitoring system:(It helps in improving the system’s security)
We introduced a concept called as monitoring system, it monitors the authorized person that he was entering the correct credentials or not, if they enter the correct credentials the system won’t disturbs them but in case any incorrect credentials are entered for couple of time’s then the monitoring system automatically activates and thinks that someone was trying to get access without the proper permission of authorized administrator or proper credentials. Then it warns the person and clicks the snap of the that person and the program closes.
Then the system automatically sends the snap along with location, data and time of the person where he tried to access the system via Email and WhatsApp.
With this information it is easy to catch the person who tried to access the system and we can make a police complaint about illegal action’s that person made with proper evidence he can’t escape because the system also send’s the IP address of the victim so its make the police men easy to catch the victim.

2)Encrypting System: (it use’s Cryptography algorithm for encryption)
Here the user details are encrypted using Cryptography algorithm (Symmetric encryption) which used one key to encrypted and decrypt the file, only authorized administrator consists of this key to decrypt the user details file to see the details of the users.
Without the actual key that we used to encrypt the file it’s not possible to decrypt the file.  Unless you decrypt the file its impossible for humans to read the data of the users.so the details of the users are highly Encrypted and Safe.
