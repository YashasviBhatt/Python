class Student:
    classVar = 'Vestibulum Facilisis'

    def __init__(self, name, roll, address):                                    # constructor
        self.name = name
        self.roll = roll
        self.address = address

    def showDetails(self):
        '''printing details of student'''
        print(f'Student Details :-\nName : {self.name}\nRoll Number : {self.roll}\nAddress : {self.address}\n')

    @classmethod
    def convertStringToObjectDetails(cls, string):
        '''this function convert string to object details'''
        # params = string.split('; ')
        # return cls(*params)                           # using *args
        return cls(*string.split('; '))                 # one liner


student1 = Student('Lorem Ipsum', '17364', 'A-17 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')
student2 = Student('Perspiciatis Unde', '17365', 'A-18 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')
student3 = Student.convertStringToObjectDetails('Aenean Tortor; 17366; A-19 Dolor Sit Amet, Consectetur Adipiscing, Volnovica')

student1.showDetails()
student2.showDetails()
student3.showDetails()