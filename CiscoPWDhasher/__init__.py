import random
import base64   
import scrypt
from backports.pbkdf2 import pbkdf2_hmac
from passlib.hash import md5_crypt
from passlib.hash import cisco_type7

# Translate Standard Base64 table to Cisco Base64 Table used in Type8 and TYpe 9                                                
std_b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
cisco_b64chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b64table = str.maketrans(std_b64chars, cisco_b64chars)


class InvalidPassword(Exception):
    """
    Exception to be thrown if an invalid password is submitted to be hashed.
    """
    pass


def pwd_check(pwd):
    """
    Checks cleartext password for invalid characters
    :param pwd: Clear text password
    :raises InvalidPassword: If the password contains invalid characters not supported by Cisco
    :return: None
    """
    invalid_chars = r"?\""
    if len(pwd) > 127:
        raise InvalidPassword('Password must be between 1 and 127 characters in length.')
    if any(char in invalid_chars for char in pwd):
        raise InvalidPassword(r'? and \" are invalid characters for Cisco passwords.')


def type5(pwd):
    """
    Hashes cleartext password to Cisco type 5
    :param pwd: Clear text password to be hashed
    :raises InvalidPassword: If the password contains invalid characters not supported by Cisco
    :return: Hashed password
    """
    pwd_check(pwd)
    return md5_crypt.using(salt_size=4).hash(pwd)


def type7(pwd):
    """
    Hashes cleartext password to Cisco type 7
    :param pwd: Clear text password to be hashed
    :raises InvalidPassword: If the password contains invalid characters not supported by Cisco
    :return: Hashed password
    """
    pwd_check(pwd)
    return cisco_type7.hash(pwd)


def type8(pwd):
    """
    Hashes cleartext password to Cisco type 8
    :param pwd: Clear text password to be hashed
    :raises InvalidPassword: If the password contains invalid characters not supported by Cisco
    :return: Hashed password
    """
    pwd_check(pwd)
    salt_chars = []
    for _ in range(14):
        salt_chars.append(random.choice(cisco_b64chars))
    salt = "".join(salt_chars)
    # Create the hash
    hash = pbkdf2_hmac("sha256", pwd.encode(), salt.encode(), 20000, 32)
    # Convert the hash from Standard Base64 to Cisco Base64
    hash = base64.b64encode(hash).decode().translate(b64table)[:-1]
    # Print the hash in the Cisco IOS CLI format
    password_string = f"$8${salt}${hash}"
    
    return password_string
    
    
def type9(pwd):
    """
    Hashes password to Cisco type 9
    :param pwd: Clear text password
    :raises InvalidPassword: If the password contains invalid characters not supported by Cisco
    :return: Hashed password
    """
    pwd_check(pwd)
    salt_chars = []
    for _ in range(14):
        salt_chars.append(random.choice(cisco_b64chars))
    salt = "".join(salt_chars)
    # Create the hash
    hash = scrypt.hash(pwd.encode(), salt.encode(), 16384, 1, 1, 32)
    # Convert the hash from Standard Base64 to Cisco Base64
    hash = base64.b64encode(hash).decode().translate(b64table)[:-1]
    # Print the hash in the Cisco IOS CLI format
    password_string = f'$9${salt}${hash}'
    return password_string
    