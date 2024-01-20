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
        self.__width = width
        """
        Raise:
            TypeError: if width not int.
            ValueError: if input value less than 0.
        """
        if not is_instance(width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        """
        Raise:
            TypeError: if height not int.
            ValueError: if input value less than 0.
        """
        if not is_instance(height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
