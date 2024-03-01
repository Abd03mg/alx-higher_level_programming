#!/usr/bin/python3
''' Rectangle Module '''
bg = __import__("7-base_geometry").BaseGeometry

class Rectangle(bg):
    ''' REactangle class that inherits from BG class.
        Attributes:
            __width: width of rect.
            __height: height of rect.
        Args:
            width: ...
            height: ...
    '''
    def __init__(self, width, height):
        bg.integer_validator(self,"width", width)
        self.__width = width
        bg.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        ''' Area function.
        Return:
            area of rect.
        '''
        return self.__width * self.__height
    def __str__(self):
        ''' String representation of class'''
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)

