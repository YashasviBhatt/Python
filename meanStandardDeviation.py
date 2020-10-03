from random import randint
import statistics as stats

lower_limit = int(input('Enter Lower Limit : '))
upper_limit = int(input('Enter Upper Limit : '))
num_of_values = int(input('Decide Number of Values to Generate : '))
values = list()

for num in range(num_of_values):
    values.append(randint(lower_limit, upper_limit))

mean = stats.mean(values)

standard_deviation = stats.stdev(values)

print([mean, standard_deviation])