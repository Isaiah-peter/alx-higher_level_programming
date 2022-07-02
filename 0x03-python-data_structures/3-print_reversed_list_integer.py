#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list) - 1
    for _ in range(len(my_list)):
        print("{:d}".format(my_list[num]))
        num = num - 1
