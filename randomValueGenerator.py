from random import randint

lower_limit = int(input('Enter Lower Limit : '))
upper_limit = int(input('Enter Upper Limit : '))
num_of_values = int(input('Decide Number of Values to Generate : '))
values = list()

for num in range(num_of_values):
    values.append(randint(lower_limit, upper_limit))

print(values)