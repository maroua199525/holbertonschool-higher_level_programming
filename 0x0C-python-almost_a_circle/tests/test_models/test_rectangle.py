"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class testclass(unittest.TestCase):
    """
    This class contains unittests for Rectangle class
    """
    def test_init(self):
        """
        method that holds the tests related to __init__ method
        """
        rectangle = Rectangle(4, 5, 6, 7, None)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 7)
        self.assertNotEqual(rectangle.id, None)

    def test_number_argument(self):
        """ checks the number of arguments """
        with self.assertRaises(TypeError):
            reslt = Rectangle()
        with self.assertRaises(TypeError):
            reslt = Rectangle(5)
        with self.assertRaises(TypeError):
            reslt = Rectangle(2, 3, 4, 6, 7, 9, 12, 13, 15)

    def test_validation(self):
        """
        method to test validation of width, height, x and y
        """
        with self.assertRaises(TypeError):
            rect = Rectangle("m", "a")
        with self.assertRaises(TypeError):
            rect = Rectangle(7, "a")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "k")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 6, 8, "f")
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 3)
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 4)
        with self.assertRaises(ValueError):
            rect = Rectangle(8, -2)
        with self.assertRaises(ValueError):
            rect = Rectangle(7, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -1, 7)
        with self.assertRaises(ValueError):
            rect = Rectangle(6, 7, 2, -9)

    def test_private_attributes(self):
        """ checks if attributes are private """
        rect = Rectangle(5, 5)
        with self.assertRaises(AttributeError):
            print(rect.__width)
        with self.assertRaises(AttributeError):
            print(rect.__height)
        with self.assertRaises(AttributeError):
            print(rect.__x)
        with self.assertRaises(AttributeError):
            print(rect.__y)

    def test_area(self):
        """ test area method """
        rect = Rectangle(9, 4)
        self.assertEqual(rect.area(), 36)

    def test_str(self):
        """ test str method """
        rect1 = Rectangle(4, 6, 2, 1, 12)
        rect2 = Rectangle(4, 4)
        string1 = str(rect1)
        string2 = str(rect2)
        self.assertEqual(string1, "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(string2, "[Rectangle] (6) 0/0 - 4/4")

    def test_update(self):
        """ test update method """
        rect1 = Rectangle(5, 5, 5, 5, 5)
        rect1.update(1)
        string = str(rect1)
        self.assertEqual(string, "[Rectangle] (1) 5/5 - 5/5")
        rect1.update(1, 1, 1, 1, 1)
        string = str(rect1)
        self.assertEqual(string, "[Rectangle] (1) 1/1 - 1/1")
