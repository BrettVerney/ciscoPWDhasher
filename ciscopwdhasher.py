import sys
import os
import random
import base64   
import scrypt
from backports.pbkdf2 import pbkdf2_hmac
from passlib.hash import md5_crypt
from passlib.hash import cisco_type7

# Translate Standard Base64 table to Cisco Base64 Table used in Type8 and TYpe 9                                                
std_b64chars  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
cisco_b64chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b64table = str.maketrans(std_b64chars, cisco_b64chars)

def banner():
    print(r'''
+------------------------------------------------------------------------+
|    ____ _                 ____                                     _   |
|   / ___(_)___  ___ ___   |  _ \ __ _ ___ _____      _____  _ __ __| |  |
|  | |   | / __|/ __/ _ \  | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |  |
|  | |___| \__ \ (_| (_) | |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |  |
|   \____|_|___/\___\___/  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  |
|                                                                        |
|           _   _           _                                            |
|          | | | | __ _ ___| |__   ___ _ __      .--.                    |
|          | |_| |/ _` / __| '_ \ / _ \ '__|    /.-. '----------.        |
|          |  _  | (_| \__ \ | | |  __/ |       \'-' .--"--""-"-'        |
|          |_| |_|\__,_|___/_| |_|\___|_|        '--'                    |
|                                                                        |
|  by: Brett Verney (@WiFiWizardOFOz)                      version: 1.0  |
+------------------------------------------------------------------------+
''')

def show_menu():
    print('Select a hashing algorithm:' + '\n')
    print('[1]  Type 5 (MD5)')
    print('[2]  Type 7 (XOR Cipher)')
    print('[3]  Type 8 (PBKDF2-HMAC-SHA256)')
    print('[4]  Type 9 (Scrypt)')        
    print('[5]  Exit')
    
def app_start(): 
    show_menu()
    try: 
        choice = int(input('\n' + 'Your selection: '))
    except ValueError:
        print ('\n' + 'Invalid option. Please enter 1-5 or press CTRL+C to exit: ' + '\n')
        app_start()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        if choice == 1:
            type5()
        elif choice == 2:
            type7()
        elif choice == 3:
            type8()
        elif choice == 4:
            type9()
        elif choice == 5:
            sys.exit()
        else:
            print ('\n' + 'Invalid option. Please enter 1-5 or press CTRL + C to exit: ' + '\n')
            app_start()

def pwd_input():
    pwd = input('\n' + 'Enter a Plain Text Password to convert: ')    
    return pwd

def pwd_check(pwd):
    invalid_chars = r"?\""
    val = True
    if len(pwd) > 127:
        print('Password must be between 1 and 127 characters in length. Please try again or press CTRL + C to exit:')
        val = False
    if any(char in invalid_chars for char in pwd):
        print('? and \" are invalid characters for Cisco passwords. Please try again or press CTRL + C to exit:')
        val = False
    if val:
        return val
    
def type5():
    valid_pwd = False
    while not valid_pwd:
        try:
            pwd = pwd_input()
        except KeyboardInterrupt:
                sys.exit(0)
        else:
                if (pwd_check(pwd)):
                    # Create the hash
                    hash = md5_crypt.using(salt_size=4).hash(pwd)
                    # Print the hash in Cisco Syntax
                    print( '\n' + f"Your Cisco Type 5 password hash is: {hash}")
                    valid_pwd = True

def type7():
    valid_pwd = False
    while not valid_pwd:
        try:
            pwd = pwd_input()
        except KeyboardInterrupt:
                sys.exit(0)
        else:
                if (pwd_check(pwd)):
                    # Create the hash
                    hash = cisco_type7.hash(pwd)
                    # Print the hash in Cisco syntax
                    print( '\n' + f"Your Cisco Type 7 password hash is: {hash}")
                    valid_pwd = True

def type8():
    valid_pwd = False
    while not valid_pwd:
        try:
            pwd = pwd_input()
        except KeyboardInterrupt:
                sys.exit(0)
        else:
                if (pwd_check(pwd)):
                    # Create random salt (Cisco use 14 characters from custom B64 table)
                    salt_chars=[]
                    for _ in range(14):
                        salt_chars.append(random.choice(cisco_b64chars))
                    salt = "".join(salt_chars)
                    # Create the hash
                    hash = pbkdf2_hmac("sha256", pwd.encode(), salt.encode(), 20000, 32)
                    # Convert the hash from Standard Base64 to Cisco Base64
                    hash = base64.b64encode(hash).decode().translate(b64table)[:-1]
                    # Print the hash in the Cisco IOS CLI format
                    print( '\n' + f"Your Cisco Type 8 password hash is: $8${salt}${hash}")
                    valid_pwd = True

def type9():
    valid_pwd = False
    while not valid_pwd:
        try:
            pwd = pwd_input()
        except KeyboardInterrupt:
                sys.exit(0)
        else:
                if (pwd_check(pwd)):
                    # Create random salt (Cisco use 14 characters from custom B64 table)
                    salt_chars=[]
                    for _ in range(14):
                        salt_chars.append(random.choice(cisco_b64chars))
                    salt = "".join(salt_chars)
                    # Create the hash
                    hash = scrypt.hash(pwd.encode(), salt.encode(), 16384, 1, 1, 32)
                    # Convert the hash from Standard Base64 to Cisco Base64
                    hash = base64.b64encode(hash).decode().translate(b64table)[:-1]
                    # Print the hash in the Cisco IOS CLI format
                    print( '\n' + f"Your Cisco Type 9 password hash is: $9${salt}${hash}")
                    valid_pwd = True

def main():
    banner()
    app_start()
         
# Start Here
if __name__ == "__main__":
    main()