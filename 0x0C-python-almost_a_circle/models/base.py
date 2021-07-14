#!/usr/bin/python3
""" Module: base
This module defines a class
"""


import json
import os


class Base:
    """ defines class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates instance attributes"""

        if id is not None:
            self.id = id
        elif id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(dicts) == dict for dicts in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        list_of_dictionaries = []
        for items in list_objs:
            list_of_dictionaries.append(items.to_dictionary())
        jsonstr = cls.to_json_string(list_of_dictionaries)
        with open(filename, 'w') as f:
            f.write(jsonstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""

        the_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            the_list = json.loads(json_string)
        return the_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """
        dummy_obj = cls(1, 1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"

        if file != None:
            with open(file, 'r') as f:
                content = cls.from_json_string(f.read())
            new_list = []#list to append the objs
            for item in content:
                dict1 = cls.create(**item)#create the obj 
                new_list.append(dict1)
            return new_list
        return []
