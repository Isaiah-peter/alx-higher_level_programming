#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
and returns X-request-id
"""
from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as respond:
            body = respond.read()
            print(body.decode("utf8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
