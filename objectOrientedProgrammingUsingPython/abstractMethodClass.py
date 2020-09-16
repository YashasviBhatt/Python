# from abc import ABCMeta, abstractmethod               # these 2 lines are used for python version older than 3.4
# class Shape(metaclass=ABCMeta):
from abc import ABC, abstractmethod
class Shape(ABC):
    '''It will bound child classes with the function.
    We can't instantiate an Abstract Class
    because its an incomplete class without any proper functionality and output for the Abstract Methods.
    these Abstract Methods are just meant for other Child Classes to be implemented.
    Thus we need a concrete subclass to get instantiated with the help of an object.'''
    @abstractmethod
    def printArea(self):
        '''All the subclasses are now bound with the rule of adding the printArea() function'''
        return 0

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printArea(self):
        '''this function override original printArea() function, if this function is not added it will throw error'''
        return self.length * self.breadth

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def printArea(self):
        '''this function override original printArea() function, if this function is not added it will throw error'''
        return self.side * self.side

rect1 = Rectangle(12, 15)
print(f'Area of Rectangle : {rect1.printArea()}')

sq1 = Square(12)
print(f'Area of Square : {sq1.printArea()}')