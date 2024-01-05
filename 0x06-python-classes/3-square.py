#!/usr/bin/python3
""" class Square """


class Square:
    """ define class square.
    Args:
        size: size of square.
    Attribute:
        __size: this attr is for the square size.
    """
    def __init__(self, size=0):
        self.__size = size
        """
        Raise:
            TypeError: if size not int.
            ValueError: if size less than zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ define area method.
        Returns:
            the current squre area.
        """
        return (self.__size * self.__size)
