[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wifiwizardofoz/ciscoType5hash)

# ciscoType5hash
A Python Cisco MD5 Password Hashing Tool

**ciscoType5hash.py**

**Author:** Brett Verney</br>
**Version:** v0.2 | 22-05-2020

This script hashes a plain text password using the MD5 algorithm used by Cisco 'Type 5' secrets. It is particularly useful in situations where an engineer wants to build a full configuration file but doesn't want to list passwords in plain text, or does not have a Cisco device available to generate the hash.

## Cisco Configuration

### Cisco IOS/IOS-XE

```username <username> secret 5 <md5_hash_password>```<br>
*or*<br>
```enable secret 5 <md5_hash_password>```
  
For example:<br>
```username admin secret 5 $1$gBk3$sBeTOYNqovq/iccFjqQoV0```<br>
*or*<br>
```enable secret 5 $1$gBk3$sBeTOYNqovq/iccFjqQoV0```

## Script Usage

### Windows

```python ciscoType5hash.py```

### MAC / OSX

```python ./ciscoType5hash.py```

**Note:**
*If you have both Python 2 and Python 3 installed you should run* ```python3 ./ciscoType5hash.py```

### Linux

```python ./ciscoType5hash.py```

**Note:**
*If you have both Python 2 and Python 3 installed you should run* ```python3 ./ciscoType5hash.py```

