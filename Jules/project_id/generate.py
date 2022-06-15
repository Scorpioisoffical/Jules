import cryptography as crypt
import cryptography.fernet as fernet
import os

def generate_key():
    if os.path.exists('Jules/key.key'):
        print('key already exists')
    else:
        if os.path.exists('Jules'):

         key = fernet.Fernet.generate_key()
         return key
        else:
            os.mkdir('Jules')
            key = fernet.Fernet.generate_key()
            return key

