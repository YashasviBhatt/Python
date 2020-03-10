def SumOfSquares(limit) :
    sum=0
    while limit>0 :
        sum=sum+(limit**2)
        limit-=1
    return sum

inpt_lim=int(input('Enter Limit : '))
print('The Sum of Squares of Numbers between 0 and {} is {}'.format(inpt_lim,SumOfSquares(inpt_lim)))