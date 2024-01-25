#!/usr/bin/python3
""" Define Class MyList that inherits from list."""


class MyList(list):
    """ Class MyList.
    ParentClass:
        list.
    Methods:
        print_sorted.
    """
    def print_sorted(self):
        """function that print sorted list"""
        print(sorted(self))
