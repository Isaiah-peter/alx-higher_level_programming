#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
  with request.urlopen("https://alx-intranet.hbtn.io/status") as respond:
    body = respond.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(body), body, body.decode("utf-8")))