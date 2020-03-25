# Program to swap values stored in 2 Variables

# creating function which will swap values stored in 2 variables
def Swap(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

var1 = int(input('Enter 1st Value : '))
var2 = int(input('Enter 1st Value : '))

print('Initial Values : {} {}'.format(var1, var2))

var1, var2 = Swap(var1, var2)

print('Final Values : {} {}'.format(var1, var2))