#   Python Password Generator
#   Python application that generates a password based on user input length
# using the formula: 50% letters, 33% digits, 17% symbols (approximately)


import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation


def user_input():
    while True:
        password_length = int(input("Enter password length: "))
        if password_length <= 5:
            print("Password must contain at least 6 characters")
        else:
            break

    total_letters = int(password_length / 2)
    total_digits = int(password_length / 3)
    total_symbols = password_length - total_letters - total_digits
    return total_letters, total_digits, total_symbols


def generate_password(tot_letters, tot_digits, tot_symbols):
    password = []
    for i in range(tot_letters):
        password.append(random.choice(letters))
    for i in range(tot_digits):
        password.append(random.choice(digits))
    for i in range(tot_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    return ''.join(password)


let, dig, sym = user_input()
print(generate_password(let, dig, sym))
