#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if (len(argv) - 1) == 1:
        print("{:d} argument:".format(len(argv) - 1))
    elif (len(argv) - 1) == 0:
        print("{:d} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    for i in range(0, len(argv)):
        if (i > 0):
            print("{:d}: {}".format(i, argv[i]))
