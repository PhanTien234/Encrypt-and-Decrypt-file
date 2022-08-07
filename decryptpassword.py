import os
import pyAesCrypt
import sys


target_file = "challenge.txt.aes"
# custom encryption/decryption buffer size ( default is 64KB)
bufferSize = 128 * 1024
# Read the passwords file
with open("xato-net-10-million-passwords-1000000.txt",'r')as fob:
    lines_list = fob.readlines()
for line in lines_list:
    pwd = line.strip("/n")
    try:
         #try to decypt
        pyAesCrypt.decryptFile("challenge.txt.aes", "challenge.txt", pwd, bufferSize)
        # Print the correct password
        print(pwd)
        break
    except ValueError as ve:
        #print(ve)
        continue