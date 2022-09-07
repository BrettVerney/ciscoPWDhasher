#!/usr/bin/env python3

# Script by Brett Verney (@wifiwizardofoz)
# Contributors - Josh Schmelzle (@joshschmelzle), Kyle Kowalczyk(@superadm1n)
# Version: v1.0 | 21-04-2021

import sys
MIN_PYTHON = (3, 6)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

from CiscoPWDhasher import pwd_check, InvalidPassword, type5, type7, type8, type9



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
|  by: Brett Verney (@WiFiWizardOFOz)                      version: 0.1  |
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
    """
    Home screen of the script. Gathers input from user to specify what type of hash they want,
    collect the cleartext password, hash that cleartext password, and print out the hash to the user.
    :return: None
    """
    show_menu()
    try: 
        choice = int(input('\n' + 'Your selection: '))
    except ValueError:
        print('\n' + 'Invalid option. Please enter 1-5 or press CTRL+C to exit: ' + '\n')
        app_start()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        if choice == 1:
            cleartext_password = pwd_input()
            hash = type5(cleartext_password)
            print(f'Your Cisco type 5 password is: {hash}')
        elif choice == 2:
            cleartext_password = pwd_input()
            hash = type7(cleartext_password)
            print(f'Your Cisco type 7 password is: {hash}')
        elif choice == 3:
            cleartext_password = pwd_input()
            hash = type8(cleartext_password)
            print(f'Your Cisco type 8 password is: {hash}')
        elif choice == 4:
            cleartext_password = pwd_input()
            hash = type9(cleartext_password)
            print(f'Your Cisco type 9 password is: {hash}')
        elif choice == 5:
            sys.exit()
        else:
            print('\n' + 'Invalid option. Please enter 1-5 or press CTRL + C to exit: ' + '\n')
            app_start()

def pwd_input():
    """
    Function to gather the input from the user until they enter a valid string that Cisco can use as a password
    :return: Password to be hashed
    """
    while True:
        pwd = input('\n' + 'Enter a Plain Text Password to convert: ')
        try:
            pwd_check(pwd)
            return pwd
        except InvalidPassword as exception_string:
            print(f'{exception_string} Please try again or press CTRL + C to exit: ')
        except KeyboardInterrupt:
            exit()


def main():
    banner()
    app_start()
         
# Start Here
if __name__ == "__main__":
    main()
