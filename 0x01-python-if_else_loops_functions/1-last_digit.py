#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = int(str(number)[-1:])
start = "Last digit of {} is {} and is {}"
last_info = ""
if last_digit > 5:
    last_info = "greater than 5"
elif last_digit == 0:
    last_info = "0"
elif last_digit < 6 and last_digit != 0:
    last_info = "less than 6 and not 0"
print(start.format(number, last_digit, last_info))
