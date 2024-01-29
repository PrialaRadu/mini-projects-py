# Python JSON to CSV
# Python application that converts data from JSON format into a CSV file


import json


try:
    with open('data-in.json', 'r') as f:
        data = json.load(f)
        categories = [key for key in data[0].keys()]
        values = []
        for obj in data:
            values.append([str(value) for value in obj.values()])

    with open('data-out.csv', 'a') as f:
        f.write(','.join(categories))
        for value in values:
            f.write(f"\n{','.join(value)}")

except Exception as e:
    print(e)
