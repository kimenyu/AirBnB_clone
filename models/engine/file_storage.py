#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



"""Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

"""

class FileStorage:
    """class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """adds new object to __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)
            
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass
