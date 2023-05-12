#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_listcp = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return(my_listcp)
    my_listcp[idx] = element
    return(my_listcp)
