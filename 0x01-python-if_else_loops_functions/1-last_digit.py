#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
text = "Last digit of "
if lastDigit > 5:
    text = text + f"{number} is {lastDigit} and is greater than 5"
elif lastDigit == 0:
    text = text + f"{number} is {lastDigit} and is 0"
else:
    text = text + f"{number} is {lastDigit} and is less than 6 and not 0"
print(text)
