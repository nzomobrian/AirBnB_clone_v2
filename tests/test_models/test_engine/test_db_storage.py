#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb
from unittest.mock import patch
import os


class TestDataBase(unittest.TestCase):
    """this will test the console"""

    @classmethod
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def startdB(self):
        self.db = MySQLdb.connect(host="localhost",
                                  user="hbnb_dev",
                                  passwd="hbnb_dev_pwd",
                                  db="hbnb_dev_db")
        self.cur = self.db.cursor()

    @classmethod
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def closedB(self):
        self.db.close()
        self.cur.close()

    @classmethod
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def setUpClass(self):
        """setup for the test"""
        self.env = patch.dict('os.environ',
                              {'HBNB_MYSQL_USER': 'hbnb_dev',
                               'HBNB_MYSQL_PWD': 'hbnb_dev_pwd',
                               'HBNB_MYSQL_HOST': 'localhost',
                               'HBNB_MYSQL_DB': 'hbnb_dev_db',
                               'HBNB_TYPE_STORAGE': 'db',
                               'HBNB_ENV': 'None'})
        with self.env:
            self.store = DBStorage()
            self.store.reload()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def teardown(self):
        """at the end of the test this will tear it down"""
        self.store.close()
        self.db.close()
        self.cur.close()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create(self):
        """ Checks if row in tables are created """

        tables = ["amenities", "cities", "places", "reviews",
                  "states", "users"]
        lens = []
        TestDataBase.startdB()
        for table in tables:
            self.cur.execute("SELECT * FROM " + table + ';')
            rows = self.cur.fetchall()
            lens.append(len(rows))

        new_state = State(name="California")
        self.store.new(new_state)
        self.store.save()

        new_city = City(name="San Francisco", state_id=new_state.id,
                        state=new_state)

        self.store.new(new_city)
        self.store.save()

        new_user = User(first_name="Larry", email="larry@m.com",
                        password="pass")

        self.store.new(new_user)
        self.store.save()

        new_place = Place(name="Lubalu", city_id=new_city.id,
                          user_id=new_user.id)

        self.store.new(new_place)
        self.store.save()

        new_amenity = Amenity(name="Wifi")

        self.store.new(new_amenity)
        self.store.save()

        new_review = Review(text="Nice", place_id=new_place.id,
                            user_id=new_user.id)

        self.store.new(new_review)
        self.store.save()

        TestDataBase.closedB()
        TestDataBase.startdB()

        new_lens = []
        for table in tables:
            self.cur.execute("SELECT * FROM " + table + ';')
            rows = self.cur.fetchall()
            new_lens.append(len(rows))

        for i in range(len(new_lens)):
            self.assertEqual(lens[i] + 1, new_lens[i])

        TestDataBase.closedB()
