#!/usr/bin/python3
"""
a test for the BaseModel class
"""
import unittest
from datetime import datetime
import models
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """a test for the BaseModel class"""

    def test_instance(self):
        """test if an instance of BaseModel is created"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_init(self):
        """test the initialization of the BaseModel class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """test the save method of the BaseModel class"""
        my_model = BaseModel()
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertGreater(my_model.updated_at, old_updated_at)

    def test_str(self):
        """test the __str__ method of the BaseModel class"""
        my_model = BaseModel()
        my_model_str = str(my_model)
        self.assertIn("BaseModel", my_model_str)
        self.assertIn("id", my_model_str)
        self.assertIn("created_at", my_model_str)
        self.assertIn("updated_at", my_model_str)

    def test_to_dict(self):
        """test the to_dict method of the BaseModel class"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn("__class__", my_model_dict)
        self.assertIn("id", my_model_dict)
        self.assertIn("created_at", my_model_dict)
        self.assertIn("updated_at", my_model_dict)

    def tearDown(self):
        """clean up the test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring(self):
        """test if the docstring is not empty."""
        self.assertIsNotNone(BaseModel.__doc__)

if __name__ == '__main__':
    unittest.main()
