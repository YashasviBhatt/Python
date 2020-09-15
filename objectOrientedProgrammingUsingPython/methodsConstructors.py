# class without constructor
class Employee:
    classVar = 'Vestibulum Facilisis'

    def showDetails(self):
        print(f'Employee Details :-\nName : {self.name}\nEmployee Id : {self.id}\nAddress : {self.address}\n')


# class with constructor
class Student:
    def __init__(self, name, roll, address):                                    # constructor
        self.name = name
        self.roll = roll
        self.address = address

    def showDetails(self):
        '''printing details of student'''
        print(f'Student Details :-\nName : {self.name}\nRoll Number : {self.roll}\nAddress : {self.address}\n')


employee1 = Employee()
employee2 = Employee()

employee1.name = 'Lorem Ipsum'
employee1.id = 'eid64'
employee1.address = 'A-17 Dolor Sit Amet, Consectetur Adipiscing, Volnovica'

employee2.name = 'Perspiciatis Unde'
employee2.id = 'eid65'
employee2.address = 'A-18 Dolor Sit Amet, Consectetur Adipiscing, Volnovica'

print('Output 1\n')

employee1.showDetails()
employee2.showDetails()

########################################################################################################

print('Output 2\n')

student1 = Student('Lorem Ipsum', 17364, 'A-17 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')
student2 = Student('Perspiciatis Unde', 17365, 'A-18 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')

student1.showDetails()
student2.showDetails()

print(f'Docstring of showDetails : {Student.showDetails.__doc__}')              # printing docstring of showDetails() function