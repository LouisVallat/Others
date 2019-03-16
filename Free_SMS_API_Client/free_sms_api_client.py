"""
This is a short Python script that you can use in order to send SMS to your
mobile phone using the FREE SMS API.

https://bit.ly/2ObREnS

@author: Louis Vallat
"""

import urllib.request as urlreq
import json

# Ask the user what message do they want to send.
TEXT = input("Your message is : ")

# FREE API USER ID
USER = 'YOUR API USER ID'

# FREE API PASSWORD
PASS = 'YOUR API PASSWORD'

# Build the data to send to the FREE API
BODY = {'user':USER, 'pass':PASS, 'msg':TEXT}

# Free API endpoint
API_ENDPOINT = "https://smsapi.free-mobile.fr/sendmsg"


# Build the request
REQUEST = urlreq.Request(API_ENDPOINT)
REQUEST.add_header('Content-Type', 'application/json; charset=utf-8')
JSONDATA = json.dumps(BODY).encode('utf-8')
REQUEST.add_header('Content-Length', len(JSONDATA))

# Send the request
RESPONSE = urlreq.urlopen(REQUEST, JSONDATA)
RESPONSE_CODE = RESPONSE.getcode()

# Tell the user if something went wrong
if RESPONSE_CODE == 200:
    print("Success!")
elif RESPONSE_CODE == 400:
    print("Missing parameter.")
elif RESPONSE_CODE == 402:
    print("Too many sms sent. Try again later.")
elif RESPONSE_CODE == 403:
    print("Free api not activated/wrong pass key.")
elif RESPONSE_CODE == 500:
    print("Internal server error. Try again later.")
else:
    print("Something went wrong.")
