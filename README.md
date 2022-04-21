[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wifiwizardofoz/ciscoPWDhasher)

# ciscoPWDhasher
An offline Cisco Password Hashing Tool for Cisco IOS/IOS-XE

**Author:** Brett Verney</br>
**Version:** v1.0 | 21-04-2022

This script converts a plain text password into a Cisco 'secret' CLI hash. It currently supports Type 5 (MD5), Type 7 (XOR Cipher), Type 8 (PBKDF2-HMAC-SHA256), and Type 9 (scrypt)

It is particularly useful in situations where an engineer wants to build a full CLI configuration file but doesn't want to list passwords in plain text, or does not have access to a Cisco device in order to generate the password hash.

## Requirements

- Python 3.6+
- Python Libraries
  - scrypt
  - backports.pbkdf2
  - passlib

## Script Usage

### Windows

```python ciscoPWDhasher.py```

### MAC / OSX

```python ./ciscoPWDhasher.py```

**Note:**
*If you have both Python 2 and Python 3 installed you should run* ```python3 ./ciscoPWDhasher.py```

### Linux

```python ./ciscoPWDhasher.py```

**Note:**
*If you have both Python 2 and Python 3 installed you should run* ```python3 ./ciscoPWDhasher.py```

## Example

The script uses an interactive menu to help choose which hash type is required. An example is below:

![ciscoPWDhasher Example](https://github.com/wifiwizardofoz/ciscoPWDhasher/blob/master/example.PNG)

## Cisco CLI Configuration

### Cisco IOS/IOS-XE

```username <username> secret {5|7|8|9} <hash>```<br>
*or*<br>
```enable secret {5|7|8|9} <hash>```
  
For example:<br>
```username admin secret 5 $1$gBk3$sBeTOYNqovq/iccFjqQoV0```<br>
*or*<br>
```enable secret 9 $9$OD7tNTjMffsK4T$x8y1enumMaDqfgNlFeI5z9KtEmiqxP90e5R632s1QNk```

## Special Thanks
[Josh Schmelzle](https://github.com/joshschmelzle/) for helping me figure out Type 8 and Type 9 requirements.</br>
[Kyle Kowalczyk](https://github.com/superadm1n/) for basically turning this in to something usuable by systems and people other than just copy and paste script n00bz.
