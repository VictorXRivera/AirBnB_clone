#!/usr/bin/python3
""" Inheriting from BaseModel """
from models.base_model import BaseModel

class User(BaseModel):
    """ User class """
    super().__init__(email, password, first_name, last_name)
