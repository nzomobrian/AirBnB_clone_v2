#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "No apply for db")
class TestDataBase(unittest.TestCase):
    """this will test the console"""
    def test_db(self):
        """ test database """
        pass
