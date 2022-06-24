#!/usr/bin/python3
import sys

# function that prints an integer
# value can any type (integer, string, etc.)
# Returns True if value has been correctly printed
# else, print message on stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
