#!/usr/bin/python3
''' Rectangle Module '''
bg = __import__('7-base_geometry').BaseGeometry

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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

