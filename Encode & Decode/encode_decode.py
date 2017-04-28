 '''
 * Copyright (C) 2017  Sw4p
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * @author Sw4p
 *
'''

import base64
import os

# Ask user for the type of encoding or decoding
print("Which type of encoding/decoding do you want to use?")
print("- Base64 | 64")
print("- Base32 | 32")
print("- Base16 | 16")
print()
codeType = int(input(">> "))

# Ask user for the type of source they will be encoding or decoding
print("What source do you want to use?")
print("- String | text")
print("- File | file")
print()
sourceType = input(">> ")

# Ask user if they want to encode or decode the source
print("Do you want to encode or decode the source?")
print("- Encode | e")
print("- Decode | d")
print()
choice = input(">> ")

# Logic

if codeType == 64:
    if sourceType == "text":
        if choice == "e":
            # Encode text with base64
            print("Enter the text you want base64 encoded: ")
            print(base64.encodestring(bytes(input(">> "), 'utf-8')).decode())
        elif choice == "d":
            # Decode text with base64
            print("Enter the text you want base64 decoded: ")
            print(base64.decodestring(bytes(input(">> "), 'utf-8')).decode())
        else:
            print("Answer can only be e or d.")
    elif sourceType == "file":
        if choice == "e":
            
            # Encode file with base64    
            print("Enter the path to the file you want base64 encoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Encoding
            with open(sourceFile) as file:
                encoded_string = base64.b64encode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(encoded_string.decode())
            print("Finished encoding!") # Finished
            
        elif choice == "d":

            # Decode file with base64
            print("Enter the path to the file you want base64 decoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Decoding
            with open(sourceFile) as file:
                decoded_string = base64.b64decode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(decoded_string.decode())
            print("Finished decoding!") # Finished
            
        else:
            print("Answer can only be e or d.")
    else:
        print("Answer can only be text/file.")
elif codeType == 32:
    if sourceType == "text":
        if choice == "e":
            # Encode text with base32
            print("Enter the text you want base64 encoded: ")
            print(base64.b32encode(bytes(input(">> "), 'utf-8')).decode())
        elif choice == "d":
            # Decode text with base32
            print("Enter the text you want base64 decoded: ")
            print(base64.b32decode(bytes(input(">> "), 'utf-8')).decode())
        else:
            print("Answer can only be e or d.")
    elif sourceType == "file":
        if choice == "e":

            # Encode file with base32
            print("Enter the path to the file you want base64 encoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Encoding
            with open(sourceFile) as file:
                encoded_string = base64.b32encode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(encoded_string.decode())
            print("Finished encoding!") # Finished
            
        elif choice == "d":

            # Decode file with base32
            print("Enter the path to the file you want base64 decoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Decoding
            with open(sourceFile) as file:
                decoded_string = base64.b32decode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(decoded_string.decode())
            print("Finished decoding!") # Finished
            
        else:
            print("Answer can only be e or d.")
    else:
        print("Answer can only be text/file.")
elif codeType == 16:
    if sourceType == "text":
        if choice == "e":
            # Encode text with base16
            print("Enter the text you want base64 encoded: ")
            print(base64.b16encode(bytes(input(">> "), 'utf-8')).decode())
        elif choice == "d":
            # Decode text with base16
            print("Enter the text you want base64 decoded: ")
            print(base64.b16decode(bytes(input(">> "), 'utf-8')).decode())
        else:
            print("Answer can only be e or d.")
    elif sourceType == "file":
        if choice == "e":

            # Encode file with base16
            print("Enter the path to the file you want base64 encoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Encoding
            with open(sourceFile) as file:
                encoded_string = base64.b32encode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(encoded_string.decode())
            print("Finished encoding!") # Finished
            
        elif choice == "d":

            # Decode file with base16
            print("Enter the path to the file you want base64 decoded: ")
            sourceFile = input(">> ")

            # Select output file
            print("Enter the path to the output file: ")
            outputFile = input(">> ")

            # Decoding
            with open(sourceFile) as file:
                decoded_string = base64.b32decode(bytes(file.read(), "utf-8")) 

            # Write to file
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open(outputFile, flags)
            with os.fdopen(filecreate, 'w') as fileCreated:
                fileCreated.write(decoded_string.decode())
            print("Finished decoding!") # Finished
            
        else:
            print("Answer can only be e or d.") # Error
    else:
        print("Answer can only be text/file.") # Error
else:
    print("Answer can only be 64/32/16.") # Error
