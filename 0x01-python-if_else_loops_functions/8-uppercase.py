#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase by adjusting ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
