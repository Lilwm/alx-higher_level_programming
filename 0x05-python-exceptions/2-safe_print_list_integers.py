#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # a function that prints the first x elements of a list and only integers.
    # if x is bigger than the list, raise an exception error

    count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return count
