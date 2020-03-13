# Program to print the largest number/element in a list

num_of_elmnts=int(input('Enter number of Elements of list : '))
initial_list=[]

if num_of_elmnts<0 :
    print('Invalid Number Entered')
elif num_of_elmnts==0 :
    print('No Elements can be Entered')
else :
    print('Enter Elements')
    initial_list=[int(input()) for inpt_elmnt in range(0,num_of_elmnts)]

print('The Largest Number Entered in the list is :')
if num_of_elmnts==1 :
    print(initial_list(0))
else :
    print(max(initial_list))        # direct approach