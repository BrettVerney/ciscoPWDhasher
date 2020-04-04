import sys
import re
from passlib.hash import md5_crypt

char = re.compile(r'[a-zA-Z0-9()!#$%^&*.,+=_-]')

def main():
    try:
        pwd = input('\n' + 'Enter a Plain Text Password to Encrypt: ')
    except KeyboardInterrupt:
            sys.exit(0)
    else:
        if len(pwd) > 64:
            print ('Password must be between 1 and 64 characters. Try again.')
            main()
        else:
            if (char.match(pwd)):
                hash = md5_crypt.using(salt_size=4).hash(pwd)
                print ('\n' +'Your MD5 Hash is: ' + (hash))
            else:
                print ('Illegal characters. Try again.')
                main()

# Start Here
if __name__ == "__main__":
    main()
