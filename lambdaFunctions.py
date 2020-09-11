swap = lambda x, y : (y, x)
subtract = lambda x, y : (x - y, y - x)
addition = lambda x, y : x + y
multiplication = lambda x, y : x * y
division = lambda x, y : (x / y, y / x)


print(swap(6, 3))
print(subtract(6, 3))
print(addition(6, 3))
print(multiplication(6, 3))
print(division(6, 3))