#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer_test.py').max_integer
    """Module to find the max integer in a list
    """
    class testmax(unittest.Testcase):
    """
    This class contains tests for the function max_integer
    """
        def test_max(self):
            self.assertEqual(max_integer([1, 2, 3, 4], 4))
            self.assertEqual(max_integer(([1, 3, 6, 2], 6))
            self.assertEqual(max_integer([1, 7, 0, -3]), 7)
            self.assertEqual(max_integer([5, 7, 9, 8, 9, 1]), 9)
            self.assertEqual(max_integer([]), None)
            with self.assertRaises(TypeError):
                max_integer(["hello", 1, 2])
