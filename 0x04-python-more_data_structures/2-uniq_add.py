#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    extra = []
    for x in my_list:
        if extra.count(x) <= 0:
            answer += x
        extra.append(x)
    return answer

