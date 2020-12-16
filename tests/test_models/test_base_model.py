#!/usr/bin/python3
"""Checking the unittest of base model Class """
from models.base_model import Base, BaseModel
import unittest
import datetime
from uuid import UUID
import json
from os import getenv
import os


class test_basemodel(unittest.TestCase):
    """Checking the unittest of base model Class """

    def __init__(self, *args, **kwargs):
        """ Instantiation of a basemodel instance"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """checking the setUp """
        pass

    def tearDown(self):
        """check the tearDown  to file jason"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ check default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ checking the kwarg values"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """checking if kwarg is an int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_save_file(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ checking srt method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """checking to dict method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ checking if not kwargs is passed """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """cheking if one key value is passed """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(type(new), self.value)

    def test_id(self):
        """ checking if id is a str"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ checking the created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """checking if the datatime is right """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
