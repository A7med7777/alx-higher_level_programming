#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = [num for num in my_list]

    if idx < 0 or idx > len(copy_list) - 1:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
