# calculator using operator overloading

class Calculator:
    '''__funcname__ are dunder methods used for operator overloading'''
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

    def __pow__(self, power, modulo=None):
        return self.num ** power.num

    def __mod__(self, other):
        return self.num % other.num

n1 = int(input('Enter Number 1 : '))
n2 = int(input('Enter Number 2 : '))

num1 = Calculator(n1)
num2 = Calculator(n2)

print(f'\nAddition : {num1 + num2}\n'
      f'Subtraction : {num1 - num2}\n'
      f'Multiplication : {num1 * num2}\n'
      f'Division : {num1 / num2}\n'
      f'Power : {num1 ** num2}\n'
      f'Modulus : {num1 % num2}')