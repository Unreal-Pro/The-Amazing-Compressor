# Created in response to a YouTube short saying that you cannot compress a file into a single byte.

import time
import random

# Compressible text:
with open("Text 1.txt") as file:
    text = file.read()

with open("Text 0.txt") as file:
    otherText = file.read()

with open("Last Compressed File.txt") as file:
    lastCompressedFile = file.read()


Option = input("Compress or decompress (1 or 2): ")

# COMPRESS
if Option == "1":
    userText = input("Insert your text file here: ")

    print("Working...")
    time.sleep(random.randint(1, 2))

#   Writes to 0
    if lastCompressedFile == "1":

#       Write file to text 0.txt
        with open("Text 0.txt", "w") as file:
            file.write(userText)

#       Change Last Compressed File.txt to 0
        with open("Last Compressed File.txt", "w") as file:
            file.write("0")

        print("Compressed file: 0")

#   Writes to 1
    elif lastCompressedFile == "0":

#       Write file to text 1.txt
        with open("Text 1.txt", "w") as file:
            file.write(userText)

#       Change Last Compressed File.txt to 1
        with open("Last Compressed File.txt", "w") as file:
            file.write("1")

        print("Compressed file: 1")

#   Failed
    else:
        print("Filed to compress.")

# DECOMPRESS
elif Option == "2":
    Option = input("Paste compressed file: ")

#   Outputs text 1
    if Option == "1":
        print("Working...")
        time.sleep(random.randint(1, 2))

        print(f"Decompressed file: {text}")

#   Outputs text 2
    elif Option == "0":
        print("Working...")
        time.sleep(random.randint(1, 2))

        print(f"Decompressed file: {otherText}")

#   Fails
    else:
        print("Working...")
        time.sleep(random.randint(0, 1))

        print("Failed to decompress.")

# User did not input 1 or 2
else:
    print("Input 1 or 2.")