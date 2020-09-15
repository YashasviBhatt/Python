print('Output 1')
class class1:
    def func1(self):
        print('Hello')

class class2:
    def func2(self):
        print('Hello World')

'''
order in multiple inheritance matter
it will look for inherited items in first class first
'''
class class3(class1, class2):                               # multiple inheritance
    def func3(self):
        print('Hello from Python')

clssss = class3()                   # instance of class2
clssss.func1()                      # calling inherited function
clssss.func2()                      # calling inherited function
clssss.func3()
print()

###################################################################

print('Output 2')

# Father class created
class Father:
    fathername = ""

    def show_father(self):
        print(self.fathername)


# Mother class created
class Mother:
    mothername = ""

    def show_mother(self):
        print(self.mothername)


# Son class inherits Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.fathername = "Lorem"
s1.mothername = "Ipsum"
s1.show_parent()