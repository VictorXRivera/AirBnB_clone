#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from uuid import UUID
import unittest


class Test_base_model(unittest.TestCase):

    def test_init(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)

    def test_str(self):
        base = BaseModel()
        string = "[{}] ({}) {}".format(type(base).__name__,
                                       base.id, str(base.__dict__))
        #fails becuase self.maxDiff is not set to none
        self.assertEqual(str(base), string)

    def test_to_dict(self):
        base = BaseModel()
        base_str = "BaseModel"
        dict_obj = base.to_dict()
        obj_key = set(dict_obj.keys())
        obj_key_2 = set(base.__dict__.keys())
        self.assertTrue(obj_key_2.issubset(obj_key))
        self.assertEqual(dict_obj["__class__"], base_str)
        self.assertTrue("__class__" in obj_key)
        self.assertIsInstance(dict_obj["created_at"], str)
        self.assertIsInstance(dict_obj["updated_at"], str)
        self.assertEqual(dict_obj["created_at"], base.updated_at.isoformat())
        self.assertEqual(dict_obj["updated_at"], base.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
