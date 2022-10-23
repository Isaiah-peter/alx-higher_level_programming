#!/usr/bin/python3
"""Write a Python script that fetches id"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    pat = argv[2]

    r = requests.get("https://api.github.com/user", auth=(username, pat))
    print(r.json().get("id"))
