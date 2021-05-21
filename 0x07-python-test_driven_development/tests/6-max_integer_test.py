#!/usr/bin/python3
import unittest
max = __import__('6-max_integer_test.py').max_integer
def max_integer(list=[]):
    """Module to find the max integer in a list
    """
    class test_max(unittest.Testcase):
        self.assertEqual(max_integer([1, 2, 3, 4], 4))
        self.assertEqual(max_integer(([1, 3, 6, 2], 6))
        self.assertEqual(max_integer([1, 7, 0, -3]), 7)
        self.assertEqual(max_integer([5, 7, 9, 8, 9, 1]), 9)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(["hello", 1, 2])
