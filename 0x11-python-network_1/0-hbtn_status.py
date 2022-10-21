#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
  with request.urlopen("https://alx-intranet.hbtn.io/status") as respond:
    res = respond.read()
    print(res)
    print("Body response:")
    print(f"    - type: {type(res)}")
    print(f"    - content: {res}")
    print(f"    - utf8 content: {res.decode('utf8')}")