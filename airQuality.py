# python api tutorial: https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json
from datetime import datetime



# Getting list of cities, doesn't need parameters, only a GET request
response1 = requests.get("https://api.openaq.org/v1/cities")
print(response1.status_code)

# JSON is a way to encode data structures that allows machines to read them easily
    # Primary way in which data is passed to/from APIs
print(response1.json())

def jprint(obj): # creates a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response1.json())


# Getting stuff that needs parameters from APIs
# this API needs parameters for lat (latitude) and long (longitude)
    # do this through adding an option keyword argument (params) to the request
    # make a dictionary with these parameters, and pass it into the requests.get()
    # you can pass the parameters directly to the API, but it's preferable to do so through 
        # using a dictionary
        # http://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74

parameters = {
    "lat": 40.71,
    "lon": -74
}
response2 = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)
jprint(response2.json())
 # documentation specified that it would return a dictionary with 3 keys, the third key (response) contains a list of pass times
 # each pass time is a dictionary with risetime (pass start time) and duration keys

# extracting pass times from the JSON object
pass_times = response2.json()['response']
jprint(pass_times)

# to extract just the 5 risetime values
risetimes = []
for p in pass_times:
    time = p['risetime']
    risetimes.append(time)
print(risetimes) # comes in a format known as a timestamp/epoch
    # which is measured in the number of seconds since 1/1/1970
    # datetime.fromtimestamp() converts to a easier to read time

times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)



