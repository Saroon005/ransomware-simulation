import os
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def get_files(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.encrypted'):
                files.append(os.path.join(root, filename))
    return files

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        ciphertext = file.read()[:-16]
        tag = file.read()[-16:]
    cipher = AES.new(key, AES.MODE_EAX, ciphertext[:16])
    data = cipher.decrypt_and_verify(ciphertext[16:], tag)
    return data

def simulate_ransomware(directory):
    files = get_files(directory)
    key = get_random_bytes(16)
    for file_path in files:
        print(f'Decrypting {file_path}')
        data = decrypt_file(file_path, key)
        with open(file_path[:-10], 'wb') as decrypted_file:
            decrypted_file.write(data)
        os.remove(file_path)
    print('Ransomware simulation complete.')

directory = 'C:/Users/YourUsername/Documents'  # Replace with your directory
simulate_ransomware(directory)
