from random import randint, choice

# copying functions
def func1():
    print('Hello')
func2 = func1               # copying function
del func1                   # deleting func1()
func2()
print()

# creating a function which will return a function
def func3(num):
    return print if num == 0 else int
print(func3(randint(0, 1)))
print()

# creating a function which will take function name as argument
def func4(func5):
    func5('Hello World')
func4(print)
print()

def func6(func7):
    lst = [12, 453, 124, 54, 11, 1, 445, 53]
    print(func7(lst))
func6(choice([max, min, sum]))
print()

################################################################################################

# executers

def outer1(caller1):
    def inner1():
        print('Executing inner1() function before calling caller1() function')
        caller1()
        print('Executing inner1() function after calling caller1() function')
    return inner1

@outer1                                                         # these lines (40, 43) works same
def final_function():
    print('Hello World')
# final_function = outer1(final_function)                       # these lines (40, 43) works same

final_function()