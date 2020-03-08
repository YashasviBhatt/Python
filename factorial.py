# Program to find the factorial of a number

def factorial(num) :
    if num == 1 :
        return num
    else :
        return num*factorial(num-1)

num = int(input('Enter Number : '))
if num<0 :
    print('Invalid Value Entered')
elif num==0 :
    print('The Factorial of 0 is',1)
else :
    print('The Factorial of {} is {}'.format(num,factorial(num)))