''' program to print * * * * *
                      * * * *
                       * * *
                        * *
                         *
'''

num_of_lines=int(input('Enter Number of Lines : '))
for star,space in zip(range(num_of_lines,0,-1),range(0,num_of_lines)) :
    print(' '*space,'* '*star)