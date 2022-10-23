#!/usr/bin/python3
"""Write a Python script that fetches id"""
import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    num = 0
    r = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name))
    for i in r.json():
        if num < 10:
            print("{}: {}\
            ".format(i.get('sha'), i.get('commit').get('author').get('name')))
        num += 1
