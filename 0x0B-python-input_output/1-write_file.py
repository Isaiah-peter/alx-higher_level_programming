#!/usr/bin/python3
"""Write To file"""


def write_file(filename="", text=""):
    """write to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
