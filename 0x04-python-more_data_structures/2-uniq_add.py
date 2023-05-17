#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for item in my_list:
        if item not in unique:
            unique.append(item)
            total += item
    return total
