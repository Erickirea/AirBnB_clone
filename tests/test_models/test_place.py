#!/usr/bin/python3
import unittest
from models import place

""""
a test module for Place class
"""
class TestPlace(unittest.TestCase):
    """
    a test class for Place class
    """
    def setUp(self):
        """
        set up place object before each test case
        """
        self.place_obj = place.Place()

    def tearDown(self):
        """
        tear down place object after each test case
        """
        del self.place_obj

    def test_str(self):
        """
        test the __str__ method
        """
        test_str = str(self.place_obj)
        self.assertIn('id', test_str)
        self.assertIn('created_at', test_str)
        self.assertIn('updated_at', test_str)
        self.assertIn('name', test_str)
        self.assertIn('description', test_str)
        self.assertIn('number_rooms', test_str)
        self.assertIn('number_bathrooms', test_str)
        self.assertIn('max_guest', test_str)
        self.assertIn('price_by_night', test_str)
        self.assertIn('latitude', test_str)
        self.assertIn('longitude', test_str)
        self.assertIn('amenity_ids', test_str)
        self.assertIn(self.place_obj, test_str)

    def test_instance(self):
        """
        test if an instance is created
        """
        self.assertIsInstance(self.place_obj, place.Place)
        self.assertTrue(hasattr(self.place_obj, 'id'))
        self.assertTrue(hasattr(self.place_obj, 'created_at'))
        self.assertTrue(hasattr(self.place_obj, 'updated_at'))
        self.assertTrue(hasattr(self.place_obj, 'name'))
        self.assertTrue(hasattr(self.place_obj, 'description'))
        self.assertTrue(hasattr(self.place_obj, 'number_rooms'))
        self.assertTrue(hasattr(self.place_obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place_obj, 'max_guest'))
        self.assertTrue(hasattr(self.place_obj, 'price_by_night'))
        self.assertTrue(hasattr(self.place_obj, 'latitude'))
        self.assertTrue(hasattr(self.place_obj, 'longitude'))
        self.assertTrue(hasattr(self.place_obj, 'amenity_ids'))

    def to_dict(self):
        """
        test the to_dict method
        """
        new_dict = self.place_obj.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertIn('id', new_dict)
        self.assertIn('name', new_dict)
        self.assertIn('created_at', new_dict)
        self.assertIn('updated_at', new_dict)
        self.assertIn('description', new_dict)
        self.assertIn('number_rooms', new_dict)
        self.assertIn('max_guests', new_dict)
        self.assertIn('number_bathrooms', new_dict)
        self.assertIn('price_by_night', new_dict)
        self.assertIn('latitude', new_dict)
        self.assertIn('longitude', new_dict)
        self.assertIn('amenity_ids', new_dict)
    
    def test_docstring(self):
        """
        test if the docstring is not empty
        """
        self.assertIsNotNone(place.Place.__doc__)

if '__name__' == '__main__':
    unittest.main()
