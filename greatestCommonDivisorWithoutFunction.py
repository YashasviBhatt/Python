# Program to print the GCD of 2 numbers without Function

num1=int(input('Enter 1st Number'))
num2=int(input('Enter 2nd Number'))

i=1

while i<=num1 and i<=num2 :
    if num1%i==0 and num2%i==0 :
        gcd=i
    i+=1
    
print(gcd)