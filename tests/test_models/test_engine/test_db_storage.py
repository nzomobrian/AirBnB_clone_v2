#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel, Base
from models.user import User


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "No apply for db")
class TestDataBase(unittest.TestCase):
    """this will test the console"""
    def test_db(self):
        """ test database """
        pass
