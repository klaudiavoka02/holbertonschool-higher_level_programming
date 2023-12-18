#!/usr/bin/python3

'''
This module provides the Square class, which inherits from Rectangle.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
Square class inherits from Rectangle.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of square's position. Default=0
            y (int, optional): Y-coordinate of square's position. Default=0
            id (int, optional): Identifier for square. Defaults=None
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for size.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size.'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns attributes based on arguments.'''
        if args:
            attr_list = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_list[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''Returns a string representation of the Square instance.'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square.'''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
