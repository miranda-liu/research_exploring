import requests
import json
from datetime import datetime

def jprint(obj): # creates a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

response4 = requests.get("https://api.openaq.org/v1/parameters")
# print(response4.status_code)
print(response4.json())

response3 = requests.get("https://api.openaq.org/v1/measurements")
# print(response3.status_code)
print(response3.json())

print("done")