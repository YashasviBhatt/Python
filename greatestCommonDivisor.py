# Program to print the GCD of 2 numbers using Function

def gcd (num1,num2) :
    if num2==0 :
        return num1
    else :
        return gcd(num2,num1%num2)
    
num1=int(input('Enter 1st Number : '))
num2=int(input('Enter 2nd Number : '))

print('The Greatest common Divisor of {} and {} is {}'.format(
        num1,num2,gcd(num1,num2)))