#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    for a in range(x):
        try:
            print(my_list[a], end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)

