#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value - 0:
            print(value)
    except TypeError:
        return False
    return True
