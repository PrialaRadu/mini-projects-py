import string


def analyze_file(file_name, encoding='utf-8'):
    try:
        with open(file_name, 'r', encoding=encoding) as f:
            data = f.read()
            res = dict()
            # Total lines
            res["total_lines"] = data.count('\n') + 1 if data.count('\n') > 0 else 0
            # Total words
            res["total_words"] = len(data.split())
            # Total characters
            res["total_characters"] = len(''.join(data.split()))
            # Total letters, digits, special characters
            res["total_letters"] = sum(1 for c in data if c in string.ascii_letters)
            res["total_digits"] = sum(1 for c in data if c in string.digits)
            res["total_specials"] = sum(1 for c in data if c in string.punctuation)
            # Unique words
            res["unique_words"] = len(set(data.split()))
            return res
    except FileNotFoundError as fe:
        print(fe)
    except IndexError as ie:
        print(ie)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)


text_file = input('Type the file path: ')
print(analyze_file(text_file))
