#!/usr/bin/env python3
import string
import random

def generateString():
    all_letters = string.ascii_letters
    digits = string.digits
    randomString = ''

    for _ in range(10):
        randomString += random.choice(all_letters)

    for _ in range(3):
        randomString += random.choice(digits)
    
    return randomString


def reverseString(forwardString):
    return forwardString[::-1]

newString = generateString()
with open('randomStringOutput.txt', 'w') as file:
    file.write(newString)
    file.write(reverseString(newString))
