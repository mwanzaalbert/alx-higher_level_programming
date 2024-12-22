#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines a class that models a student."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


class Student:
    """
    Represents a student with basic information.

    Attributes_:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args_:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student instance.

        If a list of attribute names is provided, only those attributes
        will be included in the dictionary representation.

        Args_:
            attrs (list, optional): A list of attribute names to include.
                                    Defaults to None.

        Returns_:
            dict: A dictionary representation of the student. If `attrs` is
                 provided, only
            attributes in the list that exist in the instance are included.
        """
        if isinstance(attrs, list) \
                and all(isinstance(attr, str) for attr in attrs):

            return {key: self.__dict__.get(key) for
                    key in attrs if self.__dict__.get(key)}

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args_:
            json (dict): The key/value pairs to replace attributes with.
        """
        if isinstance(json, dict):
            self.__dict__.update(json)
