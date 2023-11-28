#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = (number if number > 0 else number * -1) % 10
if number < 0:
    last = -last
print(f'Last digit of {number:d} is {last}', end=" ")
if last > 5:
    print(f'and is greater than 5')
elif last == 0:
    print(f'and is 0')
elif last < 6:
    print(f'and is less than 6 and not 0')
