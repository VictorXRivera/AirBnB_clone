#!/usr/bin/python3
'''city: inherits from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City: stores City name (empty)
    '''
    state_id = ''
    name = ''
