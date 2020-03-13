''' Program to print *
                    **
                   ***
                  ****
                 *****
'''

num_of_lines=int(input('Enter Number of Lines : '))
for star,space in zip(range(1,num_of_lines+1),range(num_of_lines-1,-1,-1)) :
    print(' '*space,'*'*star)