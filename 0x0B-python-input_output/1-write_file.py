#!/usr/bin/python3
"""Write To file"""


def write_file(filename="", text=""):
    string = str(text)
    with open(filename, 'r+', encoding="utf-8") as f:
       return f.write(string)
