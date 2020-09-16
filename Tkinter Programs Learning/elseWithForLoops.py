# only works if for loop iterate completely
num_list = [num for num in range(1, 50)]
for item in num_list:
    print(item)
else:
    print('This loop ended properly')

############################################################################################3

# Linear search using the above strategy

from random import randint

num_list = list()

# list generation
for index in range(20):
    num_list.append(randint(1, 1000))

# linear search with for-else strategy
srch_elmnt = int(input('Enter Search Element : '))
for element in range(len(num_list)):
    if element in num_list:
        print(f'Element Found at Location {num_list.index(element) + 1}')
        print(num_list)
        break
else:
    print('Not Found')