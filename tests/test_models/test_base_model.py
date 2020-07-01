#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime as dt
from uuid import UUID
import unittest


class Test_base_model(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        pass
        print("tearDown")

    def test_id(self):
        bm = self.name
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(UUID(base.id), UUID)

if __name__ == '__main__':
    unittest.main()
