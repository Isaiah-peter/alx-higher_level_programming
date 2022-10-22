#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
and returns X-request-id
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as respond:
        body = respond.read()
        print(body.decode("utf8"))
