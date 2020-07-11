#!/usr/bin/python3
""" file_storage: serializes/deserializes to/from a JSON file """
import json
import models
import os

class FileStorage:
    """ FileStorage: serialize/deserialize to/from a JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all: returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ new: sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ save: serializes __objects to the JSON file """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict.append(value.to_dict())
        with open(self.__file_path, 'w+') as a_file:
            json.dump(obj_dict, a_file)

    def reload(self):
        """reload: deserializess the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as file:
                list_of_dicts = json.loads(file.read())
        except:
            pass
