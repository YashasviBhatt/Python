print('Output 1')

class class1:
    val1 = 'this is a public variable'
    _val2 = 'this is a protected variable'
    __val3 = 'this is a private variable'

obj = class1()
print(obj.val1)
print(obj._val2)
# print(obj._val2)                  it will throw error since we are trying to print private variable
# but still if we want to print the private variable then
print(obj._class1__val3)            # name mangling (name of private variable changed by python)

print()

###################################################################################################

# attribute overriding
print('Output 2')

class A:
    classVar1 = 'Hello this is class A'                 # this is a class variable
    def __init__(self):
        self.normalVar = 'Hello this is Constructor of Class A'
        self.classVar1 = 'Hello this was a Class Variable in A but now this is an Instance Variable in A'

class B(A):
    classVar2 = 'Hello this is class B'
    classVar1 = 'Hello, This statement wont work because this is a Class Variable and' \
                'an Instance Variable of same name is already present in inherited.'

b = B()

# it will always look for instance variable irrespective of any class variable,
# simply we can say that the priority of Instance Variable is greater than class variable
print(b.classVar1)    # b.classVar1 will search for Instance Variable first and then look for other type (if Instance Variable not present)

print()

###################################################################################################

# constructor overriding
print('Output 3')

class A:
    classVar = 'Hello this is class A'                 # this is a class variable

    def __init__(self):                                 # it wont execute because of contructor overriding
        self.normalVar = 'Hello this is Constructor of Class A'
        self.classVar = 'Hello this was a Class Variable in A but now this is an Instance Variable in A'

class B(A):
    classVar = 'Hello this is class B'                # this is a class variable

    def __init__(self):
        self.normalVar = 'Hello this is Constructor of Class B'
        self.classVar = 'Hello this was a Instance Variable in A but now this is an Instance Variable in B'

b = B()

# it will always look for instance variable irrespective of any class variable,
# simply we can say that the priority of Instance Variable is greater than class variable
print(b.classVar)    # b.classVar1 will search for Instance Variable first and then look for other type (if Instance Variable not present)

print()

###################################################################################################

# handling constructor overriding
print('Output 4')

class A:
    classVar = 'Hello this is class A'                 # this is a class variable

    def __init__(self):
        self.normalVar = 'Hello this is Constructor of Class A'
        self.classVar = 'Hello this was a Class Variable in A but now this is an Instance Variable in A'
        self.var = 'Hello this is a random Variable'

class B(A):
    classVar = 'Hello this is class B'                # this is a class variable

    def __init__(self):
        super().__init__()                              # executing the constructor of super class
        self.normalVar = 'Hello this is Constructor of Class B'
        self.classVar = 'Hello this was a Instance Variable in A but now this is an Instance Variable in B'
        # super().__init__()              # it will change the value of normalVar and classVar with class A's Instance Variables

b = B()

# it will always look for instance variable irrespective of any class variable,
# simply we can say that the priority of Instance Variable is greater than class variable
print(b.classVar)    # b.classVar1 will search for Instance Variable first and then look for other type (if Instance Variable not present)
print(b.var)            # without line 84 it will throw error