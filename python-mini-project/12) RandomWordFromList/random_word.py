import random


def random_word_from_file(file_name):
    try:
        # Reads data from file
        with open(file_name, 'r') as f:
            # Reads lines from file, every line contains a word
            data = f.readlines()
            # Chooses a random word, removes any '\n' or spaces
            random_word = random.choice(data).strip()
            return random_word
    # Handles errors
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)


print(random_word_from_file('text'))
