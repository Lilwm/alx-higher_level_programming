#!/sys/usr/python3

# a function that executes a function safely
# assume fct will be always a pointer to a function
# return the result of the function

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        import sys
        print("Exception {}".format(error), file=sys.stderr)
        return None
