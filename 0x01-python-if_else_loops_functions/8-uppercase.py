#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            print(i, end="")
        elif ord(i) >= 97 and ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
    print()
