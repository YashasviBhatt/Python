lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#####################################################################################################

# printing the square of a number in list
sq = list(map(lambda x : x**2, lst))
print(f'Output 1\n{sq}\n')

#####################################################################################################

# printing the square and cube of number
operation = [lambda x : x**2, lambda x : x ** 3]

# for num in lst:
#     print(list(map(lambda func : func(num), operation)))
print(f'Output 2\n{[list(map(lambda func : func(num), operation)) for num in lst]}\n')

#####################################################################################################

# printing all elements which are greater than 5
print(f'Output 3\n{list(filter(lambda x : x > 5, lst))}\n')

#####################################################################################################

# printing addition of items from list
from functools import reduce
print(f'Output 4\n{reduce(lambda x, y : x + y, lst)}\n')

#############################################|enumerate|#############################################

# for item, index in enumerate(lst):
#     print(item, index)
print(f'Output 5\n{[(item, index) for item, index in enumerate(lst)]}\n')