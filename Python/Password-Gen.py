import string
import random

from numpy import number
from sympy import numbered_symbols

letters = list(string.ascii_letters)
numbers = list(string.digits)
specialCharacters = list("!@#$%^&*()")

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():
    passwordLength = int(input("Please enter password length: "))

    letters_count = int(input("Please enter letter count in your password: "))
    number_count = int(input("Please enter the number of digits you would like in your password: "))
    special_Characters_count = int(input("Please enter the number of special characters you would like in your password: "))

    characters_count = letters_count + number_count + special_Characters_count

    if (characters_count > passwordLength)
        print("Characters total count is greater than the password length.")
        return

    password = []
    
    for i in range(letters_count):
        password.append(random.choice(letters))

    for i in range(number_count):
        password.append(random.choice(numbers))
    
    for i in range(specialCharacters):
        password.append(random.choice(specialCharacters))


    if characters_count < passwordLength:
        random.shuffle(characters)
        for i in range(passwordLength - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_password()


