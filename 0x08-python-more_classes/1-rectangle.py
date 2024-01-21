#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ define class Rectange.
    Attribute:
        __width: private instance attr that describes width of rec.
        __heigh: private instance attr that describes height of rec.
    Args:
        width: input value of width.
        height: input value of height.
    """
    def __init__(self, width=0, height=0):
        """instanation with width and height attr"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width attr getter
        Return:
            value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width atrr setter.
        Args:
            value: new value of atrr.
        """

        """
        Raise:
            TypeError: if width not int.
            ValueError: if input value less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height attr getter
        Return:
            value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height atrr setter.
        Args:
            value: new value of atrr.
        """

        """
        Raise:
            TypeError: if height not int.
            ValueError: if input value less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
