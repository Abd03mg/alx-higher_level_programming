#!/usr/bin/python3
""" class Square """


class Square:
    """ define class square.
    Args:
        size: size of square.
        position: position of square.
    Attribute:
        __size: this attr is for the square size.
        __position: this attr is for the square position.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """
        Raise:
            TypeError: if size not int.
            ValueError: if size less than zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """ define position method.
        Returns:
            position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """define position setter
        Args:
            value: value of new position.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ define area method.
        Returns:
            the current squre area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ define function that print the square with character '#'.
        """
        for x in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print("{}".format(" "), end="")
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
        if self.__size == 0:
            print()

    def __str__(self):
        """ define function that print the same as my_print.
        Returns:
            empty str.
        """
        if self.__size != 0:
            for x in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print("{}".format(" "), end="")
            for j in range(self.__size):
                print("{}".format("#"), end="")
            if i != self.__size - 1:
                print()
        return ("")
