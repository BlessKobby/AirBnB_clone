#!/usr/bin/python3

"""Test for the amenity model."""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing the Amenity class"""

    def test_Amenity_inheritence(self):
        """Tests that the Amenity class Inherits from BaseModel"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Tests that Amenity class had name attribute."""
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """Tests that Amenity class had name attribute's type."""
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
