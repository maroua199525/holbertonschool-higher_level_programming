#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    len1 = len(my_list)
    for i in range(0, len1):
        if my_list[i] == search:
            new[i] = replace
    return(new)
