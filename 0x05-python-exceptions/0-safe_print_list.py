#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for j in range(x):
        try:
            print(my_list[j], end="")
            num += 1
        except IndexError:
            break
    print("")
    Return

