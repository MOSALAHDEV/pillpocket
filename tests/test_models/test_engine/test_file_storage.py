#!/usr/bin/python3
"""
Testcases for FileStorage class
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testcases for FileStorage class"""
    def setUp(self):
        """ setup test environment """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """teardown test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """test all method"""
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIn(f'BaseModel.{self.model.id}', objs)

    def test_new(self):
        """test new method"""
        objs = self.storage.all()
        self.assertIn(f'BaseModel.{self.model.id}', objs)

    def test_save(self):
        """test save method"""
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn(f'BaseModel.{self.model.id}', data)

    def test_reload(self):
        """test reload method"""
        model = BaseModel()
        model.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn(f'BaseModel.{model.id}', objs)


if __name__ == "__main__":
    unittest.main()