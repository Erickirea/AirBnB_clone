#!/usr/bin/python3
import unittest
from models import user

""""
a test module for User class
"""
class TestUser(unittest.TestCase):
    """
    a test class for User class
    """
    def setUp(self):
        """Set up user object before each test case."""
        self.user_obj = user.User()

    def tearDown(self):
        """Delete user object after each test case."""
        del self.user_obj

    def test_str(self):
        """test the __str__ method."""
        self.assertEqual(str(self.user_obj), "[User] ({}) {}".format(
            self.user_obj.id, self.user_obj.__dict__))
        self.assertIsInstance(self.user_obj.__str__(), str)

    def test_instance(self):
        """test if an instance is created."""
        self.assertIsInstance(self.user_obj, user.User)
        self.assertTrue(hasattr(self.user_obj, 'id'))
        self.assertTrue(hasattr(self.user_obj, 'created_at'))
        self.assertTrue(hasattr(self.user_obj, 'updated_at'))
        self.assertTrue(hasattr(self.user_obj, 'email'))
        self.assertTrue(hasattr(self.user_obj, 'password'))
        self.assertTrue(hasattr(self.user_obj, 'first_name'))
        self.assertTrue(hasattr(self.user_obj, 'last_name'))

    def test_docstring(self):
        """test if the docstring is not empty."""
        self.assertIsNotNone(user.User.__doc__)

if __name__ == "__main__":
    unittest.main()
