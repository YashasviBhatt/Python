# By  considering  the  terms  in  the  Fibonacci  sequence  whose  values  do  not exceed four million,
# Program to find the sum of Even-Valued terms

def fib_srs(n) :
    i,j,sum1=0,1,0
    sum=i+j
    while sum<=n :
        if sum%2==0 :
            sum1=sum1+sum
            i=j
            j=sum
            sum=i+j
        else :
            i=j
            j=sum
            sum=i+j
    print(sum1)
        
n=4000000
fib_srs(4000000)
