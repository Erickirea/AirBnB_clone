#!/usr/bin/python3
import unittest
from models import review

""""
a test module for Review class
"""

class TestReview(unittest.TestCase):
    """Test class for Review class"""

    def test_instance(self):
        """test if an instance is created"""
        r = review.Review()
        self.assertIsInstance(r, review.Review)
        
    def test_init(self):
        """test the initialization."""
        r = review.Review()
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'created_at'))
        self.assertTrue(hasattr(r, 'updated_at'))
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))

    def test_str(self):
        """test the __str__ method."""
        r = review.Review()
        r_str = r.__str__()
        self.assertIsInstance(r_str, str)
    
    def test_to_dict(self):
        """test the to_dict method."""
        r = review.Review()
        r_dict = r.to_dict()
        self.assertIsInstance(r_dict, dict)
        self.assertTrue('id' in r_dict)
        self.assertEqual(type(r_dict['id']), str)
        self.assertTrue('created_at' in r_dict)
        self.assertEqual(type(r_dict['created_at']), str)
        self.assertTrue('updated_at' in r_dict)
        self.assertEqual(type(r_dict['updated_at']), str)
        self.assertTrue('place_id' in r_dict)
        self.assertEqual(type(r_dict['place_id']), str)
        self.assertTrue('user_id' in r_dict)
        self.assertEqual(type(r_dict['user_id']), str)
        self.assertTrue('text' in r_dict)
        self.assertEqual(type(r_dict['text']), str)

if '__main__' == __name__:
    unittest.main()
