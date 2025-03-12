#!/usr/bin/python3
""" FileStorage class for serializing and
deserializing instances to and from JSON files."""
import json
from models.base_model import BaseModel
from models.user import User
from models.medication import Medication
from models.order import Order


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file specified by __file_path."""
        with open(self.__file_path, "w") as f:
            new_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file specified by __file_path to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
                classes = {
                    "BaseModel": BaseModel,
                    "User" : User,
                    "Medication" : Medication,
                    "Order" : Order
                }
                for k, v in new_dict.items():
                    class_name = v.get("__class__", None)
                    class_name = class_name
                    if class_name and class_name in classes:
                        self.__objects[k] = classes[class_name](**v)
        except (FileNotFoundError, json.JSONDecodeError):
            pass