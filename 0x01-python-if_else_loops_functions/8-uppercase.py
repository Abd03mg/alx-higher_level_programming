#!/usr/bin/python3
def uppercase(str):
    st = ""
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            pass
        elif ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        st += i
    print(st)
