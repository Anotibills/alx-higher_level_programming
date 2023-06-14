#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for a, b in temp.items():
        if value == b:
            a_dictionary.pop(a)
    return my_dict
