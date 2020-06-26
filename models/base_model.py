#!/usr/bin/python3
'''Basemodel class'''
from datetime import datetime


class BaseModel:
    '''BaseModel: defines all commmon attributes/methods for other classes
    '''
    def __init__(self, id):
        '''__init__: instantiation of id, created_at, and updated_at
        '''
        self.id = uuid4(str(id))
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        '''__str__: returns the string representation
        '''
        return "[BaseModel] (%d) <%s>".format(self.id, self.__dict__)
