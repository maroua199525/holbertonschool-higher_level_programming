"""
Unittest for Square class
"""
import unittest
from models.Square import Square


class testclass(unittest.TestCase):
    """
    This class contains unittests for Square class
    """
    def test_init(self):
        """
        method that holds the tests related to __init__ method
        """
        Square = Square(4, 5, 6, 7, None)
        self.assertEqual(Square.size, 4)
        self.assertEqual(Square.x, 6)
        self.assertEqual(Square.y, 7)
        self.assertNotEqual(Square.id, None)

    def test_number_argument(self):
        """ checks the number of arguments """
        with self.assertRaises(TypeError):
            reslt = Square()
        with self.assertRaises(TypeError):
            reslt = Square(5)
        with self.assertRaises(TypeError):
            reslt = Square(2, 3, 4, 6, 7, 9, 12, 13, 15)

    def test_validation(self):
        """
        method to test validation of width, height, x and y
        """
        with self.assertRaises(TypeError):
            rect = Square("m", "a")
        with self.assertRaises(TypeError):
            rect = Square(7, "a")
        with self.assertRaises(TypeError):
            rect = Square(1, 2, "k")
        with self.assertRaises(TypeError):
            rect = Square(1, 6, 8, "f")
        with self.assertRaises(ValueError):
            rect = Square(8, 3)
        with self.assertRaises(ValueError):
            rect = Square(-1, 4)
        with self.assertRaises(ValueError):
            rect = Square(8, -2)
        with self.assertRaises(ValueError):
            rect = Square(7, 0)
        with self.assertRaises(ValueError):
            rect = Square(4, 5, -1, 7)
        with self.assertRaises(ValueError):
            rect = Square(6, 7, 2, -9)

    def test_private_attributes(self):
        """ checks if attributes are private """
        rect = Square(5, 5)
        with self.assertRaises(AttributeError):
            print(rect.__size)
        with self.assertRaises(AttributeError):
            print(rect.__x)
        with self.assertRaises(AttributeError):
            print(rect.__y)

    def test_area(self):
        """ test area method """
        rect = Square(9, 4)
        self.assertEqual(rect.area(), 36)

    def test_str(self):
        """ test str method """
        rect1 = Square(4, 6, 2, 1, 12)
        rect2 = Square(4, 4)
        string1 = str(rect1)
        string2 = str(rect2)
        self.assertEqual(string1, "[Square] (12) 2/1 - 4/6")
        self.assertEqual(string2, "[Square] (6) 0/0 - 4/4")

    def test_update(self):
        """ test update method """
        rect1 = Square(5, 5, 5, 5, 5)
        rect1.update(1)
        string = str(rect1)
        self.assertEqual(string, "[Square] (1) 5/5 - 5/5")
        rect1.update(1, 1, 1, 1, 1)
        string = str(rect1)
        self.assertEqual(string, "[Square] (1) 1/1 - 1/1")
