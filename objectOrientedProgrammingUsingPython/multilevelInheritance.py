print('Output 1')
class class1:
    def func1(self):
        print('Hello')

class class2(class1):
    def func2(self):
        print('Hello World')
        obj1 = class2()
        obj1.func1()

class class3(class2):
    def func3(self):
        print('Hello from python')
        obj2 = class3()
        obj2.func2()

obj3 = class3()
obj3.func3()

print()

##########################################################################################

print('Output 2')


class Electronic_device():
    power_source = "Alternating current or Direct Current"
    use = "Automates works and make the work very faster and efficient"
    start = "It is a kind of device which uses"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}".capitalize()


class Pocket_gadget(Electronic_device):
    power_source = "Direct current"
    addon_features = "It is portable and looks super awesome"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


class Phone(Pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


computer = Electronic_device()
miband = Pocket_gadget()
redmi = Phone()

print(computer.printdetails())
print(miband.printdetails())
print(redmi.printdetails())

print()

##########################################################################################

print('Output 3')


class Family:
    def show_family(self):
        print("This is our family:")


# Father class inherited from Family
class Father(Family):
    fathername = ""

    def show_father(self):
        print(self.fathername)


# Mother class inherited from Family
class Mother(Family):
    mothername = ""

    def show_mother(self):
        print(self.mothername)


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.fathername = "Lorem"
s1.mothername = "Ipsum"
s1.show_family()
s1.show_parent()