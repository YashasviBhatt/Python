# Program to print Fibonacci Series upto the limit set by user

num=int(input('Enter Limit : '))

# Function which will generate the list of Fibonacci Series
def fib(num) :
    sum = 0
    fib_srs=[0,1]
    i=0
    j=1
    while sum<num :
        sum=i+j
        fib_srs.append(sum)
        if sum>num :
            fib_srs.remove(sum)             # remove() function will pop that value stored in list which is passed as parameter
        i=j
        j=sum
    return fib_srs

fib_srs=fib(num)
print(fib_srs)