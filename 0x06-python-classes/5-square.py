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

    @property
    def size(self):
        """ size attr getter.
        Return:
            value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size attr setter.

        Args:
            value: new value of size.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ define area method.
        Returns:
            the current squre area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ define function that print the square with character '#'.
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
        if self.__size == 0:
            print()
