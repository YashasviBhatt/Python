# class declaration
class Student:
    classVar = 'Vestibulum Facilisis'                                   # this is a class variable

# creating objects of class Student
student1 = Student()                    # first object
student2 = Student()                    # second object

# creating instance variable of class
student1.name = 'Lorem Ipsum'
student1.roll = 17364
student1.address = 'A-17 Dolor Sit Amet, Consectetur Adipiscing, Volnovica'
student1.classVar = 'Morbi Hendrerit'                        # only change value of variable for student1 object

student2.name = 'Perspiciatis Unde'
student2.roll = 17365
student2.address = 'A-18 Dolor Sit Amet, Consectetur Adipiscing, Volnovica'
student2.classVar = 'Maecenas Mattis'                        # only change value of variable for student2 object

print(f'Student 1 Details :-\nName : {student1.name}\nRoll Number : {student1.roll}\nAddress : {student1.address}\n')
print(f'Student 2 Details :-\nName : {student2.name}\nRoll Number : {student2.roll}\nAddress : {student2.address}\n')

print(f'Printing Class Variable : {Student.classVar}')
print(f'Printing Class Variable for student 1 object : {student1.classVar}')
print(f'Printing Class Variable for student 2 object : {student2.classVar}\n')
# Student.classVar = 'Ipsum Sollicitudin'                         # changes value of variable for all the objects
# print(Student.classVar)

print(student1.__dict__)                                # prints out all the instance variable of object with its value in a dictionary
print(student2.__dict__)                                # prints out all the instance variable of object with its value in a dictionary