#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The following module defines the `Rectangle` class, a subclass of `Base`.

The `Rectangle` class represents a 2D rectangle with attributes for width,
height, and position (`x`, `y`). It provides methods for validation,
area calculation, string representation, and serialization.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-25"
__version__ = "1.1"

from models.base import Base


class Rectangle(Base):
    """
    Rectangle shape representation.

    Represents a rectangle with width, height, and position (x, y).
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args_:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position (default: 0).
            y (int): The y-coordinate of the rectangle's position (default: 0).
            id (int): The ID of the rectangle (default: None).

        Raises_:
            TypeError: If any attribute is not an integer.
            ValueError: If width or height <= 0, or if x or y < 0.
        """
        # Validate arguments
        Rectangle.validate_attribute("width", width)
        Rectangle.validate_attribute("height", height)
        Rectangle.validate_attribute("x", x)
        Rectangle.validate_attribute("y", y)

        super().__init__(id)  # Call Base class constructor for ID management

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Properties for width, height, x, and y with validation
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value, /):
        """
        Set the width of the rectangle.

        Args_:
            value (int): The new width.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        Rectangle.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value, /):
        """
        Set the height of the rectangle.

        Args_:
            value (int): The new height.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        Rectangle.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value, /):
        """
        Set the x-coordinate of the rectangle.

        Args_:
            value (int): The new x-coordinate.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        Rectangle.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value, /):
        """
        Set the y-coordinate of the rectangle.

        Args_:
            value (int): The new y-coordinate.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        Rectangle.validate_attribute("y", value)
        self.__y = value

    @staticmethod
    def validate_attribute(name, value):
        """
        Validate attributes according to the specified rules.

        Args_:
            name (str): The name of the attribute (e.g., "width").
            value (int): The value of the attribute.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value <= 0 for width/height or < 0 for x/y.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name in ("width", "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ("x", "y") and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns_:
            int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def display(self):
        """
        Print shape to stdout.

        Print the rectangle using the `#` character, considering `x` and `y`
        offsets.
        """
        print("\n" * self.y, end="")  # Print vertical offset

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Update attributes using positional or keyword arguments.

        Args_:
            *args: New values for id, width, height, x, and y (in order).
            **kwargs: Key-value pairs of attributes to update.

        Raises_:
            ValueError: If an invalid attribute is passed in kwargs.
        """
        original_values = {"id": self.id, "width": self.width,
                           "height": self.height, "x": self.x, "y": self.y}

        attr_names = ("id", "width", "height", "x", "y")
        params = {}

        try:
            # Update from args
            if args:
                params.update(dict(zip(attr_names, args)))

            # Update from kwargs
            if kwargs:
                for key in kwargs:
                    if key not in attr_names:
                        raise ValueError(
                            f"Invalid attribute '{key}' in kwargs")
                params.update(kwargs)

            # Validate and update attributes
            for attr_name, attr_value in params.items():
                if attr_name == "id":
                    Rectangle.validate_id(attr_value)
                else:
                    Rectangle.validate_attribute(attr_name, attr_value)
                setattr(self, attr_name, attr_value)

        except Exception as e:
            # Roll back to original values on error
            for key, value in original_values.items():
                setattr(self, key, value)
            raise e

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns_:
            dict: A dictionary representation of the rectangle.
        """
        attr_names = [attr for attr in dir(self) if not callable(
            getattr(self, attr)) and not attr.startswith('_')]

        return {attr: getattr(self, attr) for attr in attr_names}

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns_:
            str: A string in the format: [Rectangle] (id) x/y - width/height.
        """
        return f"[{self.__class__.__name__}] ({self.id}) " +\
            f"{self.x}/{self.y} - {self.width}/{self.height}"
