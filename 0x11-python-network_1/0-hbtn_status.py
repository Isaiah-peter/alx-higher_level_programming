#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
  with request.urlopen("https://alx-intranet.hbtn.io/status") as respond:
      print("Body response:")
      print(f"    - type: <class 'bytes'>")
      print(f"    - content: b'{respond.__dict__.get('msg')}'")
      print(f"    - utf8 content: {respond.__dict__.get('msg')}")