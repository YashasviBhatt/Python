# Program to find the sum of elements of a tuple/list

initial_tuple=()
num_of_elements=int(input('Enter Number of Elements you want to insert\n'))
sum=0
print('Enter Elements')
tup_ptr=0
while tup_ptr<num_of_elements :
    inpt_elmnt=int(input())
    sum=sum+inpt_elmnt
    tup_ptr+=1

print('The Addition of Values Entered by user is',sum)