#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base


class testclass(unittest.TestCase):
    """
    This class contains unittests for Base class
    """
    def test_id(self):
        """
        method to test id related to Base class
        """
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base(5)
        self.assertEqual(base.id, 5)
