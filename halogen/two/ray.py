# import necessary libraries
import os
from cryptography.fernet import fernet

# define a function to search for encrypted files

def search_for_encrypted_files():
    encrypted_files = []

    for root, dirs, files in os.walk("C:/"):
        for file in files:
            if file.endswith(".encrypted"):
                encrypted_files.append(os.path.join(root, file))
    return encrypted_files

# define a function to decrypt an encrypted file

def decrypt_file(filepath, key):
    with open(filepath, "rb") as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filepath[:-10], "wb") as f:
        f.write(decypted_data)
    os.remove(filepath)

# define the private key to use for decryption

PRIVATE_KEY = b"YOUR_PRIVATE_KEY_HERE"

# search for encrypted files on a system

encrypted_files = search_for_encrypted_files()

# decrypt each encrypted file using the private key

for file in encrypted_files:
    decrypt_file(file, PRIVATE_KEY)

# print a message indicating that the decryption is complete

print("Decryption Complete")
