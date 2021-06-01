#!/usr/bin/python3
""" Module MyList"""


class MyList(list):
    """
    The class MyList inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
