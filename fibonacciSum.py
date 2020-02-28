# By  considering  the  terms  in  the  Fibonacci  sequence  whose  values  do  not exceed four million,
# Program to find the sum of Even-Valued terms

num=4000000
def fib(num) :
    sum = 0
    fib_srs=[0,1]
    i=0
    j=1
    while sum<num :
        sum=i+j
        fib_srs.append(sum)
        if sum>num :
            fib_srs.remove(sum)
        i=j
        j=sum
    return fib_srs

fib_srs=fib(num)
sum=0
for i in fib_srs :
    if i%2==0 :
        print(i,end='  ')               # end is a delimiter used to separate value by any symbol
        sum+=i
print("\n",sum)