# list comprehension

# program to print a list of all the number in range of 1 to 100
print('List 1 :', [num for num in range(1, 101)])

# program to print a list of all the items divisible by 5 in range of 1 to 100
print('List 2 :', [num for num in range(1, 101) if num % 5 == 0])

print()

################################################################################################

# tuple comprehension

# program to print a tuple of all the number in range of 1 to 100
print('Tuple 1 :', tuple(num for num in range(1, 101)))

# program to print a tuple of all the items divisible by 5 in range of 1 to 100
print('Tuple 2 :', tuple(num for num in range(1, 101) if num % 5 == 0))

print()

################################################################################################

# dictionary comprehension

# program to print a dictionary of all the number in range of 1 to 100 having key as i and value as item i
print('Dictionary 1 :', {num: f'Item {num}' for num in range(1, 101)})

# program to print a dictionary of all the number in range of 1 to 100 divided by 5 having key as i and value as item i
print('Dictionary 2 :', {num: f'Item {num}' for num in range(1, 101) if num%5 == 0})

# program to print a dictionary having key as numeric numbers and value as their string counterparts, eg - 1: 'one', 2: 'two' ... so on
number_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
print('Dictionary 3 :', {num: num_str for num, num_str in zip(range(1, 11), number_string)})

# program to reverse the Dictionary 3
print('Dictionary 4 :', {num_str: num for num, num_str in zip(range(1, 11), number_string)})

print()

#################################################################################################

# set comprehension

# program to print a set of all the number in range of 1 to 100
print('Set 1 :', {num for num in range(1, 101)})

# program to print a set of all the number in range of 1 to 100 divisible by 5
print('Set 2 :', {num for num in range(1, 101) if num%5 == 0})

# program to print a set of all the items from a list
print('Set 3 :', {item for item in ['Lorem', 'Lorem', 'Ipsum', 'Dolor', 'Ipsum', 'Sit', 'Amet', 'Dolor']})

print()

#################################################################################################
#
# # generator comprehension
#
# # program to print a generator iterable of all the number in range of 1 to 100
# num_list = (num for num in range(1, 101))
# for n in num_list:
#     print(n, end=' ')