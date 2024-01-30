#   Python Password Generator
#   Python application that generates a password based on user input length
# using the formula: 50% letters, 33% digits, 17% symbols (approximately)


import random
import string


def get_password_requirements():
    # Retrieves and validates user password length
    while True:
        password_length = int(input("Enter password length: "))
        if password_length <= 5:
            print("Password must contain at least 6 characters")
        else:
            break

    # Returns total characters requirements
    total_letters = int(password_length / 2)
    total_digits = int(password_length / 3)
    total_specials = password_length - total_letters - total_digits
    return total_letters, total_digits, total_specials


def generate_password(total_letters, total_digits, total_specials):
    password = []

    # Appends random letters
    for _ in range(total_letters):
        password.append(random.choice(string.ascii_letters))
    # Appends random digits
    for _ in range(total_digits):
        password.append(random.choice(string.digits))
    # Appends random special characters
    for _ in range(total_specials):
        password.append(random.choice(string.punctuation))

    # Shuffles the list containing all characters
    random.shuffle(password)

    # Returns the password as a string
    return ''.join(password)


letters, digits, specials = get_password_requirements()
print(generate_password(letters, digits, specials))
