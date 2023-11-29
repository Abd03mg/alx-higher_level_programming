#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return (1)
    elif b == 1:
        return (a)
    if b > 0:
        p = a * pow(a, (b - 1))
    elif b < 0:
        p = (a * pow(a, (-b) - 1))
        p = 1 / p
    return p
