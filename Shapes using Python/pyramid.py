''' Program to print *
                    * *
                   * * *
                  * * * *
                 * * * * *
'''

num_of_lines=int(input('Enter Number of Lines : '))
for space,star in zip(range(num_of_lines-1,-1,-1),range(1,num_of_lines+1)) :
    print(' '*space,'* '*star)
