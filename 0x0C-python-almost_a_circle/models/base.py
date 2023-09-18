#!/usr/bin/python3
"""
The module contains the "Base" class
"""

import csv
import json
import turtle

class Base: 
    """Base class for managing id attribute across all classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy 

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        loaded_instances = []
        try:
            with open(filename, 'r') as f:
                loaded_instances = cls.from_json_string(f.read())
            for i, e in enumerate(loaded_instances):
                loaded_instances[i] = cls.create(**loaded_instances[i])
        except:
            pass
        return loaded_instances
