#!/usr/bin/python3
def safe_print_division(a, b):
    c = 1
    try:
        c = (a / b)
    except ZeroDivisionError:
        print("Inside result: None")
        return (None)
    finally:
        pass
    print("Inside result:{}".format(c))
    return (c)
