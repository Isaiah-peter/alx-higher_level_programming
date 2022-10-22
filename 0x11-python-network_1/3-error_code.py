#!/usr/bin/python3
"""Handling Error"""
from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv

url = argv[1]

if __name__ == "__main__":
    try:
        with urlopen(url) as respond:
            body = respond.read()
            print(body.decode("utf8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
