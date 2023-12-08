#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = []

    for number in my_list:
        if number in summation:
            pass
        else:
            summation.append(number)

    return sum(summation)
