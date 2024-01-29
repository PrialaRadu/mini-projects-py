"""
JSON = JavaScript Object Notation
Used for data exchange between a server and a web application
"""

import json

data = {
  "name": "John Doe",
  "age": 25,
  "isStudent": False,
  "courses": ["Math", "History", "English"],
  "address": {
    "city": "New York",
    "zipcode": "10001"
  }
}

json_string = json.dumps(data)

data_string = json.loads(json_string)
print(json_string, data_string)
