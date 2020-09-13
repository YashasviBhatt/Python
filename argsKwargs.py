from random import randint
print('Output 1 :')
def func1(*args):
    [print(name) for name in args]
func1(*[f'Name {number}' for number in range(1, 11)])
print()

#######################################################################################

print('Output 2 :')
def func2(**kwargs):
    [print(roll, name, sep = ' is ') for roll, name in kwargs.items()]
details = {f'Roll Number {roll_number}': f'Name {name_number}' for roll_number, name_number in zip(range(5), range(6, 11))}
func2(**details)