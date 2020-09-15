print('Output 1')
class class1:
    def func1(self):
        print('Hello')

class class2(class1):                       # inheritance
    def func2(self):
        print('Hello World')

clssss = class2()                   # instance of class2
clssss.func1()                      # calling inherited function
clssss.func2()
print()

########################################################################################333

print('Output 2')
# Parent class created
class Parent:
    parentname = ""
    childname = ""

    def show_parent(self):
        print(self.parentname)


# Child class created inherits Parent class
class Child(Parent):
    def show_child(self):
        print(self.childname)


ch1 = Child()  # Object of Child class
ch1.parentname = "Lorem"  # Access Parent class attributes
ch1.childname = "Ipsum"
ch1.show_parent()  # Access Parent class method
ch1.show_child()  # Access Child class method