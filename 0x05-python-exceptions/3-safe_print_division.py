#!/usr/bin/python3
def safe_print_division(a, b):
    c = 1
    try:
        c = (a / b)
    except ZeroDivisionError:
        pass
    finally:
        if b != 0:
            print("Inside result:{}".format(c))
            return (c)
        else:
            print("Inside result: None")
            return (None)
