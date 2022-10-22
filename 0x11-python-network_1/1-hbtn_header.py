#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
and returns X-request-id
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as respond:
        print(respond.headers.get("X-Request-Id"))