#!/usr/bin/python3
'''Basemodel class'''
from datetime import datetime as dt
from uuid import uuid4


class BaseModel:
    '''BaseModel: defines all commmon attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''__init__: instantiation of id, created_at, and updated_at
        '''
        from models.__init__ import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, dt.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == '__class__':
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''__str__: returns the string representation
        '''
        return "[{}] ({}) <{}>".format(type(self).__name__,
                                       self.id, self.__dict__)

    def save(self):
        '''save: updates the public instance attribute updated_at
        '''
        from models.__init__ import storage

        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        '''to_dict: returns a dictionary containing all keys/value
        of __dict__ of the instance'''
        new_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict["__class__"] = type(self).__name__
        return new_dict
