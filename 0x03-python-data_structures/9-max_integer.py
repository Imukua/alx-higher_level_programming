#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return(none)
    a = my_list[0]
    for item in my_list:
        if item > a:
            a = item
    return(a)
