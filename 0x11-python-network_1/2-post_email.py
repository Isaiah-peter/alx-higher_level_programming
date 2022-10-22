#!/usr/bin/python3
""" python script that takes in a
URL and an email, sends aPOST request the passed URL with
the email as a parameter, and displays
the body of the respons
"""
import urllib.request
import urllib.parse
from sys import argv

url = argv[1]
value = {"email": argv[2]}

data = urllib.parse.urlencode(value)
data = data.encode("ascii")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as respond:
    body = respond.read()
    print(body.decode("utf8"))
