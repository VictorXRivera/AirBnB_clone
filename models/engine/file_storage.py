#!/usr/bin/python3
""" file_storage: serializes/deserializes to/from a JSON file """
from models.base_model import BaseModel
import json


class FileStorage:
    """ FileStorage: serializes/deserializes to/from a JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all: returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ new: sets in __objects the obj with key <obj class name>.id """
        self.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """ save: serializes __objects to the JSON file """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict.append(value.todict())
        with open(self.__file_path, 'w+') as a_file:
            json.dump(obj_dict, a_file)

    def reload(self):
        """ reload: deserializess the JSON file to __objects """
        classes = {'BaseModel': BaseModel}
        
        try:
            with open(self.__file_path, 'r') as a_file:
                obj_dict = json.load(a_file)
            for key, val in obj_dict.items():
                if val["__class__"] in classes.key():
                    FileStorage.__objects[key] = classes[val["__class__"]](**val)
            else:
                FileStorage.__objects[key] = None
        except:
            pass
