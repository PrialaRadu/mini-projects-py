# Python JSON to CSV
# Python application that converts data from JSON format into a CSV file


import json


def json_to_csv(json_file, csv_file):
    try:
        # Reads data from json file
        with open(json_file, 'r') as f:
            data = json.load(f)
            categories = [key for key in data[0].keys()]
            values = []
            for obj in data:
                values.append([str(value) for value in obj.values()])

        # Writes data into the csv file
        with open(csv_file, 'a') as f:
            f.write(','.join(categories))
            for value in values:
                f.write(f"\n{','.join(value)}")

    # Handles Errors
    except FileNotFoundError:
        print(f"File not found")
    except json.decoder.JSONDecodeError:
        print(f"Invalid")
    except TypeError:
        print(f"Invalid")
    except Exception as e:
        print(e)


json_to_csv('data_in.json', 'data_out.csv')
