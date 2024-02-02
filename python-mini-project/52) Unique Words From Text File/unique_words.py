# Python Unique words from file
# Application that reads words from a text file and returns all the unique words in sorted order


import re


def unique_words(file_path):
    try:
        with open(file_path, 'r') as f:
            # Finds words using re, converts all words to lowercase, returns a sorted set (unique words)
            return sorted(set(re.findall(r'\w+', f.read().lower())))
    # Error Handling
    except FileNotFoundError:
        print('File not found')
    except UnicodeEncodeError:
        print('File encoding error')
    except Exception as e:
        print(e)


my_file_path = 'text'
print(unique_words(my_file_path))
