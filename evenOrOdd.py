def EvenOdd(num) :
    if num%2 == 0 :
        return 'EVEN'
    else :
        return 'ODD'

num=int(input('Enter Number : '))
if num == 0 :
    print('Neither Even or Odd')
else :
    result=EvenOdd(num)
    print(result)