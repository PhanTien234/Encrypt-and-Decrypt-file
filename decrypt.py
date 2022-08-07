
import pyAesCrypt
import sys
import os

# Choose the target directory
target_dir = "D:\\temp\\"
print(target_dir)
# custom encyption/decryption buffer size (default is 64KB)
bufferSize = 128 * 1024
# Input the password for encryption
password = input("Please input the p: ")
# Select every files in target dir
for path, subdirs, files in os.walk(target_dir):
    for name in files:
        origin_path = os.path.join(path, name)
        decrypted_path = os.path.join(path, name.strip(".aes"))
        try:
            # Encypte the file
            pyAesCrypt.decryptFile(origin_path, decrypted_path, password, bufferSize)
            # remove the original files
            os.remove(origin_path)
        except Exception as b:
            print(b)
