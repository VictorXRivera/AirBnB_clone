#!/usr/bin/python3
'''review: inherits from BaseModel'''
from models.base_model import BaseModel


class Review (BaseModel):
    '''Review: stores reviews on places (empty)
    '''
    place_id = ''
    user_id = ''
    text = ''
