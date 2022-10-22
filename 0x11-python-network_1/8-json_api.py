#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1] != None:
        data = {"q": argv[1]}
    else:
        data = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", params=data)
    if r != None:
        print(f"[{r.id}] {r.name}")
    else:
        print("No result")
