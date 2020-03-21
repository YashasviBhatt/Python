# Sum of Primes : A Naive Approach

limit=int(input('Enter Limit'))
f=0
sum=2
for p in range(3,limit) :
    for p1 in range(2,p) :
        if p%p1 == 0 :
            f=1
            break
    if f==0 :
        sum+=p
    else :
        f=0
print(sum)