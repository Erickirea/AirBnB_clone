#!/usr/bin/python3
import unittest
from models import city

"""Test module for City Model."""

class TestCity(unittest.TestCase):
    """Test class for City class and its methods."""

    def setUp(self):
        """Set up city instance"""
        self.city_obj = city.City()

    def tearDown(self):
        """Tear down city instance"""
        del self.city_obj

    def test_str(self):
        """test the __str__ method."""
        test_str = str(self.city_obj)
        self.assertIn('id', test_str)
        self.assertIn('created_at', test_str)
        self.assertIn('updated_at', test_str)
        self.assertIn('name', test_str)
        self.assertIn(self.city_obj, test_str)

    def test_instance(self):
        """test if an instance is created."""
        self.assertIsInstance(self.city_obj, city.City)
        self.assertTrue(hasattr(self.city_obj, 'id'))
        self.assertTrue(hasattr(self.city_obj, 'created_at'))
        self.assertTrue(hasattr(self.city_obj, 'updated_at'))
        self.assertTrue(hasattr(self.city_obj, 'name'))

    def to_dict(self):
        """test the to_dict method."""
        self.assertIsInstance(self.city_obj.to_dict(), dict)
        self.assertTrue('id' in self.city_obj.to_dict())
        self.assertEqual(type(self.city_obj.to_dict()['id']), str)
        self.assertTrue('created_at' in self.city_obj.to_dict())
        self.assertEqual(type(self.city_obj.to_dict()['created_at']), str)
        self.assertTrue('updated_at' in self.city_obj.to_dict())
        self.assertEqual(type(self.city_obj.to_dict()['updated_at']), str)
    I   self.assertTrue('name' in self.city_obj.to_dict())
        self.assertEqual(type(self.city_obj.to_dict()['name']), str)

    def test_docstring(self):
        """test if the docstring is not empty."""
        self.assertIsNotNone(city.City.__doc__)

if __name__ == '__main__':
    unittest.main()
