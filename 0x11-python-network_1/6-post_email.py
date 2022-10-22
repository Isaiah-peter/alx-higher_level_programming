#!/usr/bin/python3
""" sends a post request to the URL and displays the body
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    r = requests.post(url, data)
    print(r.text)
