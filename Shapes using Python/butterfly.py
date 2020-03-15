''' Program to print *        *
                     **      **
                     ***    ***
                     ****  ****
                     **********
                     ****  ****
                     ***    ***
                     **      **
                     *        *
'''

num_of_lines=int(input('Enter Number of Lines : '))
num_of_spaces=num_of_lines-1
# since print statement put a default space after every value passed in it
# like if we are to execute this statement print('x','y')
# the resultant output will be x y rather than xy thus we have to use sep delimiter
# whatever the value of delimiter sep is, the print statement will print that value after each value passed in it for printing
# sep='' means there should not be any space after the 0th ,1st ,2nd, ... (and so on) values printed
x=[print('*'*star,' '*space,'*'*star,sep='') for star,space in zip(range(1,num_of_lines+1),range(num_of_spaces*2,-1,-2))]
y=[print('*'*star,' '*space,'*'*star,sep='') for star,space in zip(range(num_of_lines-1,0,-1),range(2,num_of_lines*2,2))]