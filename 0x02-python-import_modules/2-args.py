#!/usr/bin/python3

# prevent code from being executed when imported
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv[1:])
    index = 1

    if arg_count == 0:
        print(" 0 arguments.")
    else:
        if arg_count == 1:
            print(" 1 argument:")
        else:
            print("{} arguments:".format(arg_count), end="\n")
        for argument in sys.argv[1:]:
            print("{}: {}".format(index, argument), end="\n")
            index = index + 1
