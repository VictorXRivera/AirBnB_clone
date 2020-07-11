#!/usr/bin/python3
""" file_storage: serializes/deserializes to/from a JSON file """
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
import json


class FileStorage:
    """ FileStorage: serialize/deserialize to/from a JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all: returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ new: sets in __objects the obj with key <obj class name>.id """
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

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

            for obj_dict in list_of_dicts:
                if obj_dict['__class__'] == "BaseModel":
                    from models.base_model import BaseModel
                    self.new(BaseModel(**obj_dict))
                if obj_dict['__class__'] == "User":
                    from models.user import User
                    self.new(User(**obj_dict))
                if obj_dict['__class__'] == "City":
                    from models.city import City
                    self.new(City(**obj_dict))
                if obj_dict['__class__'] == "Amenity":
                    from models.amenity import Amenity
                    self.new(Amenity(**obj_dict))
                if obj_dict['__class__'] == "State":
                    from models.state import State
                    self.new(State(**obj_dict))
                if obj_dict['__class__'] == "Place":
                    from models.place import Place
                    self.new(Place(**obj_dict))
                if obj_dict['__class__'] == "Review":
                    from models.review import Review
                    self.new(Review(**obj_dict))
        except:
            pass
