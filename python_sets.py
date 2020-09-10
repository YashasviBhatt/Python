s = {1, 1, 2, 3, 4, 5}
print(s)

# set will store only distinct value and ignore duplicate values


# typecasting to set

lst = [1, 2, 3, 4]
st = set(lst)

print(st)

print('Intersection :', s.intersection(st))
print('Union :', s.union(st))
print('Difference :', s.difference(st))
