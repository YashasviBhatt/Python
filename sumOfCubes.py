def SumOfCubes(limit) :
    sum=0
    while limit>0 :
        sum=sum+(limit**3)
        limit-=1
    return sum

inpt_lim=int(input('Enter Limit : '))
print('The Sum of Squares of Numbers between 0 and {} is {}'.format(inpt_lim,SumOfCubes(inpt_lim)))