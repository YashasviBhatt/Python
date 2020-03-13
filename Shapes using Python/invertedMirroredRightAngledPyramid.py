''' program to print *****
                      ****
                       ***
                        **
                         *
'''

num_of_lines=int(input('Enter Number of Lines : '))
for space,star in zip(range(0,num_of_lines),range(num_of_lines,0,-1)) :
    print(' '*space,'*'*star)
    