#!/usr/bin/python3
""" Module contain one class: Base"""
import json

class Base:
    """ Base class"""
    __nb_objects = 0
    """ private class attribute __nb_objects"""
    def __init__(self, id=None):
        """ init function """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return A JSON STRING a representation list_dict..
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write Json Representation of String
        """
        lst = []
        with open(cls.__name__ + ".json", "w", encoding="UTF-8") as f:
            if list_objs is not None:
                for x in list_objs:
                    lst.append(x.to_dictionary())
            f.write(cls.to_json_string(d))
    @staticmethod
    def from_json_string(json_string):

        """ returns the list of the JSON string representation json_string
        """
        if (json_string == None or json_string == ""):
            return []
        return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        
        """ function  that returns an instance with all attributes already set"""
        Square(size):

