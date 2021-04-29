#!/usr/bin/python3
import sys
argv = sys.argv
if (len(argv) - 1) != 1:
    print("{:d} arguments:".format(len(argv) - 1))
else:
    print("{} argument:".format(len(argv) - 1))
for i in range(0, len(argv)):
    if (i > 0):
        print("{:d}: {}".format(i, argv[i]))
