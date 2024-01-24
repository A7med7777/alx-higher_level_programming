#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        number_of_elements = (len(my_list) + 1) * -1

        for num in range(-1, number_of_elements, -1):
            print("{:d}".format(my_list[num]))
