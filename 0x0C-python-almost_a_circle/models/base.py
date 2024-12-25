#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Base class module.

This module defines the `Base` class, which serves as the foundation for
other geometric classes such as `Rectangle` and `Square`.

It provides methods for object serialization and deserialization in JSON
and CSV formats, ID management, and basic shape drawing using Turtle graphics.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-25"
__version__ = "1.1"

import os
import json
import csv
import turtle as t
import random


class Base:
    """
    Base class.

    Base class for managing ID assignment and providing common functionality
    for derived classes such as Rectangle and Square.
    """

    # Private class attribute to track the number of instances
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args_:
            id (int, optional): The unique identifier for the instance.
                                If None, an auto-generated ID is assigned.
        """
        if id is not None:
            Base.validate_id(id)  # Validate the provided ID
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def validate_id(id):
        """
        Validate the ID to ensure it is a positive integer.

        Args_:
            id (int): The ID to validate.

        Raises_:
            TypeError: If the ID is not an integer.
            ValueError: If the ID is less than or equal to 0.
        """
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        if id <= 0:
            raise ValueError("id must be > 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args_:
            list_dictionaries (list): A list of dictionaries to serialize.

        Returns_:
            str: A JSON string representation of the list.
        """
        if list_dictionaries and isinstance(list_dictionaries, list):
            return json.dumps(list_dictionaries)

        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file in JSON format.

        Args_:
            list_objs (list): A list of instances derived from Base.
        """
        file_name = f"{cls.__name__}.json"

        if isinstance(list_objs, list) \
                and all(isinstance(obj, cls) for obj in list_objs) \
                and list_objs is not None:

            list_dictionaries = [cls.to_dictionary(obj) for obj in list_objs]

            json_string = cls.to_json_string(list_dictionaries)

            if not os.path.exists(file_name):
                with open(file_name, 'w') as outfile:
                    outfile.write(json_string)

            else:
                with open(file_name, 'r') as infile:
                    data = json.load(infile)

                with open(file_name, 'w', ) as outfile:
                    data.extend(list_dictionaries)

                    json_string = cls.to_json_string(data)

                    outfile.write(json_string)
        else:
            with open(file_name, 'w') as outfile:
                outfile.write(cls.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string into a list of dictionaries.

        Args_:
            json_string (str): A JSON string representation of a list of
                              dictionaries.

        Returns_:
            list: A list of dictionaries.
        """
        if json_string is not None and isinstance(json_string, str):
            return json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class using attr's provided in the dict.

        Args_:
            dictionary (dict): A dictionary of attributes to initialize the
            instance.

        Returns_:
            object: An instance of the class.
        """
        shape = cls(10, 10) if cls.__name__ == "Rectangle" else cls(10)

        cls.update(shape, **dictionary)

        return shape

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns_:
            list: A list of instances of the class.
        """
        file_name = f"{cls.__name__}.json"

        if not os.path.exists(file_name):
            return []

        with open(file_name, 'r') as infile:
            list_dictionaries = cls.from_json_string(infile.read())

        return [cls.create(**obj) for obj in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a file in CSV format.

        Args_:
            list_objs (list): A list of instances derived from Base.
        """
        file_name = f"{cls.__name__}.csv"

        if cls.__name__ == "Rectangle":
            field_names = ["id", 'width', 'height', "x", "y"]

        if cls.__name__ == "Square":
            field_names = ["id", "size", "x", "y"]

        if isinstance(list_objs, list) \
                and all(isinstance(obj, cls) for obj in list_objs) \
                and list_objs is not None:

            list_dictionaries = [cls.to_dictionary(obj) for obj in list_objs]

            if not os.path.exists(file_name):
                # write heading
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()

                    for row in list_dictionaries:
                        writer.writerow(row)

            else:
                with open(file_name, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    data = list(reader)

                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()

                    data.extend(list_dictionaries)

                    for row in data:
                        writer.writerow(row)

        else:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns_:
            list: A list of instances of the class.
        """
        file_name = f"{cls.__name__}.csv"

        if not os.path.exists(file_name):
            return []

        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            list_dictionaries = [
                {key: int(value) for key, value in row.items()}
                for row in reader]

        return [cls.create(**obj) for obj in list_dictionaries]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using Turtle graphics.

        Args_:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        # Helper function to draw a rectangle.
        def draw_rectangle(x, y, width, height, color_f='white'):
            """
            Draw a colored rectangle.

            Args:_
                x(int): The x-coordinate of the top-left corner of the
                        rectangle/square.
                y(int): The y-coordinate of the top-left corner of the
                        rectangle/square.
                width(int): Width of the rectangle/square.
                height(int): Height of the rectangle/square.
                color_f(str, optional): Fill color of the rectangle/square.
                                         Defaults to 'white'.

            Returns:_
                None
            """
            t.shape('classic')

            t.up()
            t.goto(x, y)  # Start at bottom-left corner of rectangle
            t.fillcolor(color_f)
            t.begin_fill()
            t.down()
            t.goto(x + width, y)  # Draw line to bottom-right corner.
            t.goto(x + width, y + height)  # Draw line to top-right corner.
            t.goto(x, y + height)  # Draw line to top-left corner.
            t.goto(x, y)  # Draw line to bottom-left corner.
            t.end_fill()

            t.up()

        colors = ('green', 'red', 'blue', 'light blue')

        for shape in list_rectangles:
            draw_rectangle(shape.x, shape.y, shape.width,
                           shape.height, random.choice(colors))  # draw frame
            t.speed(0)

        for shape in list_squares:
            draw_rectangle(shape.x, shape.y, shape.width,
                           shape.height, random.choice(colors))  # draw frame
            t.speed(1)

        t.home()
        t.done()


if __name__ == "__main__":
    from models.rectangle import Rectangle
    from models.square import Square

    list_rectangles = [Rectangle(100, 40), Rectangle(
        90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
