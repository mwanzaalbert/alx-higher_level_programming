#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The following module defines the `Square` class, a subclass of `Rectangle`.

The `Square` class represents a geometric square with attributes for size,
position (`x`, `y`), and ID. It inherits from the `Rectangle` class but
ensures that width and height are always equal (represented as `size`).
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-25"
__version__ = "1.1"

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square shape representation.

    Represents a square, inheriting attributes and methods from the `Rectangle`
    class.

    The `Square` class overrides some behaviors to ensure width and height are
    equal, represented as the `size` attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args_:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square's position (default: 0).
            y (int): The y-coordinate of the square's position (default: 0).
            id (int): The ID of the square (default: None).

        Raises_:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size <= 0, or x or y < 0.
        """
        # Initialize as a rectangle with width and height equal to size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns_:
            int: The size of the square (equivalent to width or height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args_:
            value (int): The new size of the square.

        Raises_:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        Rectangle.validate_attribute("width", value)  # Validate size as width
        self.width = self.height = value  # Update both width and height

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args_:
            *args: Positional arguments in the order:
                   - id (int)
                   - size (int)
                   - x (int)
                   - y (int)
            **kwargs: Key-value pairs of attributes to update.

        Raises_:
            ValueError: If an invalid attribute is passed in kwargs.
        """
        original_values = {"id": self.id, "size": self.size,
                           "x": self.x, "y": self.y}

        attr_names = ("id", "size", "x", "y")
        params = {}

        try:
            # Update from args
            if args:
                # Map positional args to attributes
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
                elif attr_name == "size":
                    Rectangle.validate_attribute("width", attr_value)
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
        Convert the square's attributes to a dictionary representation.

        Excludes the `height` and `width` attributes as they are redundant.

        Returns_:
            dict: A dictionary representation of the square, including:
                  - id
                  - size
                  - x
                  - y
        """
        excluded_attr = ('height', 'width')

        attr_names = [attr for attr in dir(self) if not callable(
            getattr(self, attr)) and not attr.startswith('_')
            and attr not in excluded_attr]

        return {attr: getattr(self, attr) for attr in attr_names}

    def __str__(self):
        """
        Return the string representation of the square.

        Returns_:
            str: A string in the format:
                 [Square] (id) x/y - size
        """
        return f"[{self.__class__.__name__}] ({self.id}) " +\
            f"{self.x}/{self.y} - {self.width}"
