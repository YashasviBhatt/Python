class Salary:
    '''__funcname__ are known as duncder methods particularly used for operator overloading and object value management'''
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

    def __add__(self, other):                           # this is a dunder method
        return self.amount + other.amount

    def __repr__(self):
        '''this is used to briefly describe the object'''
        return f'Salary({self.amount}, \'{self.type}\')'

    def __str__(self):
        '''this is used to summarise the object'''
        return f'Salary is {self.amount}, Type of Salary is {self.type}'

main_sal = Salary(50000, 'Main Salary')
other_sal = Salary(20000, 'Tution Salary')

print(main_sal + other_sal)                             # operator overloading
print()

print(main_sal)                         # always call __str__()
print(other_sal)                        # always call __str__()
print()

# to call __repr__()
print(repr(main_sal))
print(repr(other_sal))

'''

# Program to add more than 2 objects

class A:
    def __init__(self, number):
        self.num = number
    def __add__(self, other):
        return self.num + other.num

a1 = A(12)
a2 = A(15)
a3 = A(17)

lst = [a1, a2, a3]              # list of objects
sum = 0

for i in range(1, len(lst)):    # iterating over list of objects
    sum = lst[i] + lst[i - 1]   # adding 2 value at a time and storing it to an other variable for future uses

print(sum)

'''