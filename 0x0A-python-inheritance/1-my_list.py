#!/usr/bin/python3
"""
first inheritance
"""


class MyList(list):
    """class name"""

    def print_sorted(self):
        """sort items"""
        arr = list(self)
        arr.sort()
        print(arr)
