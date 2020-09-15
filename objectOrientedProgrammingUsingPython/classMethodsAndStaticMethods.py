class Student:
    classVar = 'Vestibulum Facilisis'
    value = 0

    def __init__(self, name, roll, address):                                    # constructor
        self.name = name
        self.roll = roll
        self.address = address

    def showDetails(self):
        '''printing details of student'''
        print(f'Student Details :-\nName : {self.name}\nRoll Number : {self.roll}\nAddress : {self.address}\n')

    @classmethod                                # classmethod decorator
    def change_classvariable(cls, newClassVar):           # decorator didn't take self as argument instead it take class as argument
        '''this decorator function is made to make changes to class variable for all object'''
        cls.classVar = newClassVar

    @staticmethod                               # static method
    def printdetails():
        '''static method did not take any default argument'''
        Student.value += 1
        return f'Message from Student {Student.value} : Good Bye! Have a nice Day'


student1 = Student('Lorem Ipsum', 17364, 'A-17 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')
student2 = Student('Perspiciatis Unde', 17365, 'A-18 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')

student1.showDetails()
student2.showDetails()

print(f'Value of Class Variable before changing it is {Student.classVar}')

# all the lines below do the same work
Student.change_classvariable('Ipsum Sollicitudin')                  # change value of variable for all objects
# student1.change_classvariable('Ipsum Sollicitudin')                 # change value of variable for all objects
# student2.change_classvariable('Ipsum Sollicitudin')                 # change value of variable for all objects

# print(student1.classVar)
# print(student2.classVar)
print(f'Value of Class Variable after changing it is {Student.classVar}\n')

# print(Student.printdetails())
print(student1.printdetails())
print(student2.printdetails())