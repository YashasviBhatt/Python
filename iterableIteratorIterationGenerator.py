'''
Iterable ==> defined with __iter__() or __getitem__()
Iterator ==> defined with __next__()
Iteration ==>
Generator ==> Iterators which can be traversed only one
yield ==> generate value in real time (to save RAM)
'''

# these are the examples of generators which generate the iterator but print them as per requirement
# both these examples are showing same output

print('Output 1 : ')

strng = 'loremipsum'

itr = iter(strng)
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')

print('\n')

#################################################################################################

print('Output 2 : ')
def string(s):
    for c in s:
        yield c                     # suspend the loop

itr = string('loremipsum')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')
print(itr.__next__(), end='')