#!/usr/bin/python3
""" sends a post request to the URL and displays the body
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
