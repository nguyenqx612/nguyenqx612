import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
specialCharacters = list("!@#$%^&*()")

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():
    passwordLength = int(input("Please enter password length: "))

    letters_count = int(input("Please enter letter count in your password: "))
    number_count = int(input("Please enter the number of digits you would like in your password: "))
    special_Characters_count = int(input("Please enter the number of special characters you would like in your password: "))

    random.shuffle(specialCharacters)

    password = []
    for i in range(passwordLength):
        password.append(random.choice(specialCharacters))

    random.shuffle(password)

    print("".join(password))

generate_password()


