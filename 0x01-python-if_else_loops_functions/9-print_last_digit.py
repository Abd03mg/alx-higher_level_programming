#!/usr/bin/python3
def print_last_digit(number):
    r = ((number % 10) if number >= 0 else ((number * -1) % 10))
    print(r, end="")
    return (r)
