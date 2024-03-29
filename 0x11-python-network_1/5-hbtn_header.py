#!/usr/bin/python3
""" sends a request to the URL and displays the value X-Request-Id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
