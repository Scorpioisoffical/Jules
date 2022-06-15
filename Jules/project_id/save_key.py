from generate import generate_key
from cryptography.fernet import Fernet
import cryptography as crypt

global key

def save_key(key):
    with open('Jules/key.key', 'wb') as key_file:
        key_file.write(key)