'''program to print *
                   * *
                  * * *
                 * * * *
                * * * * *
                 * * * *
                  * * *
                   * *
                    *
'''

max_stars=int(input('Enter Number of Max Stars : '))
for space,star in zip(range(max_stars-1,-1,-1),range(1,max_stars+1)) :
    print(' '*space,'* '*star)
for space,star in zip(range(1,max_stars),range(max_stars-1,0,-1)) :
    print(' '*space,'* '*star)
