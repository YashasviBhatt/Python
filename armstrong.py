# Program to check whether the number is Armstrong or Not

num=int(input('Enter Number : '))
check=num
sum_of_armstrong=0
while num>=1 :
    sum_of_armstrong=sum_of_armstrong+(num%10)**3
    num=int(num/10)
if sum_of_armstrong==check :
    print('Armstrong Number')
else :
    print('Not an Armstrong Number')