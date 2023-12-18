#!/usr/bin/python3

'''
This module provides the Rectangle class, which inherits from Base.
'''

from models.base import Base


class Rectangle(Base):
    '''
Rectangle class inherits from Base.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of rectangle's position. Default=0
            y (int, optional): Y-coordinate of rectangle's position. Default=0
            id (int, optional): Identifier for rectangle. Defaults=None
        '''
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Getter method for width.'''
        return self.__width

    @width.setter
    def width(self, parameter_name):
        '''Setter method for width.'''
        self.check_integer_parameter(parameter_name, 'width')
        self.__width = parameter_name

    @property
    def height(self):
        '''Getter method for height.'''
        return self.__height

    @height.setter
    def height(self, parameter_name):
        '''Setter method for height.'''
        self.check_integer_parameter(parameter_name, 'height')
        self.__height = parameter_name

    @property
    def x(self):
        '''Getter method for x.'''
        return self.__x

    @x.setter
    def x(self, parameter_name):
        '''Setter method for x.'''
        self.check_integer_parameter(parameter_name, 'x')
        self.__x = parameter_name

    @property
    def y(self):
        '''Getter method for y.'''
        return self.__y

    @y.setter
    def y(self, parameter_name):
        '''Setter method for y.'''
        self.check_integer_parameter(parameter_name, 'y')
        self.__y = parameter_name

    def check_integer_parameter(self, value, parameter_name):
        '''
        Validates if a parameter is an integer.

        Args:
            value: The value to check.
            parameter_name (str): The name of the parameter.

        Raises:
            TypeError: If the value is not an integer.
        '''
        if type(value) is not int:
            raise TypeError(parameter_name + ' must be an integer')

        if value <= 0 and parameter_name in ('width', 'height'):
            raise ValueError(parameter_name + ' must be > 0')

        if value < 0 and parameter_name in ('x', 'y'):
            raise ValueError(parameter_name + ' must be >= 0')

    def area(self):
        '''Returns the area value of the Rectangle instance.'''
        return self.__width * self.__height

    def display(self):
        '''
        Prints the Rectangle instance with the character # to stdout.
        '''
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        '''
        Returns a string representation of the Rectangle instance.
        '''
        return (
                f'[Rectangle] ({self.id}) '
                f'{self.__x}/{self.__y} - {self.__width}/{self.__height}'
        )

    def update(self, *args, **kwargs):
        '''
        Assigns key/value argument to attributes.
        Args:
            *args: Arguments to be assigned in order (id, width, height, x, y).
            **kwargs: Key/value arguments to be assigned.
        '''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle.'''
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }