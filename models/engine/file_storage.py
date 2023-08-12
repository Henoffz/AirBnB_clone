#!/usr/bin/python3
"""
This is file storage program of the airbnb clone
project that uses json format for serialization
and deserialization.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file 
    and deserializes JSON file to instances
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_dic = dict()
        for key, val in self.__objects.items():
            dic[key] = val.to_dict()
        with open(self.__file_path, "w") as MyFile
            json.dump(my_dic, MyFile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as MyFile:
                 new_obj = json.load(MyFile)
            for key, val in reloj.items()
             reloj = self.class_dict[val['__class__']](**val)
              self.__objects[key] = reloj
        except FileNotFoundError:
            pass
