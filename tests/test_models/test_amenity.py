#!/usr/bin/python3
import unittest
from models import amenity

"""Test class for Amenities Model."""

class TestAmenities(unittest.TestCase):
    """Test class for Amenities Model."""

    def setUp(self):
        """Set up amenity instance."""
        self.my_amenity = amenity.Amenity()

    def tearDown(self):
        """Deletes the amenity instance."""
        del self.my_amenity

    def test_str(self):
        """test the __str__ method."""
        my_amenity = amenity.Amenity()
        my_amenity_str = str(my_amenity)
        self.assertIn("Amenity", my_amenity_str)
        self.assertIn("id", my_amenity_str)
        self.assertIn("created_at", my_amenity_str)
        self.assertIn("updated_at", my_amenity_str)

    def test_instance(self):
        """test if an instance is created."""
        my_amenity = amenity.Amenity()
        self.assertIsInstance(my_amenity, amenity.Amenity)

    def test_init(self):
        """test the initialization."""
        my_amenity = amenity.Amenity()
        self.assertTrue(hasattr(my_amenity, 'id'))
        self.assertTrue(hasattr(my_amenity, 'created_at'))
        self.assertTrue(hasattr(my_amenity, 'updated_at'))
        self.assertTrue(hasattr(my_amenity, 'name'))

    def test_docstring(self):
        """test if the docstring is not empty."""
        self.assertIsNotNone(amenity.Amenity.__doc__)

if __name__ == '__main__':
    unittest.main()
