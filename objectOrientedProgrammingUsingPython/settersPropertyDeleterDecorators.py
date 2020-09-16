class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explainEmployee(self):
        return f'Name of Employee is {self.fname} {self.lname}'

    @property
    def email(self):
        '''it will not change the value of fname and lname in the original object'''
        if self.fname == None or self.lname == None:
            return 'Email not Set'
        return f'{self.fname}.{self.lname}@123.com'

    @email.setter
    def email(self, string):
        '''it will change the value of fname and lname in the original object'''
        names = string.split('@')[0]
        fname = names.split(',')[0]
        lname = names.split('.')[1]

    @email.deleter
    def email(self):
        '''it will delete the value of fname and lname from original object'''
        self.fname = None
        self.lname = None

emp1 = Employee('Lorem', 'Ipsum')
emp2 = Employee('Dolor', 'Sit Amet')

print(emp1.explainEmployee())
print(emp2.explainEmployee())

emp1.fname = 'Dorem'
print(emp1.email)         # since the object was created before changing new name but property decorator made the changes to created object
emp1.email = 'hello.world@python.com'       # it wont work without line 14
print(emp1.fname)
print(emp1.lname)
print(emp1.email)

del emp1.email      # deleting email

print(emp1.email)