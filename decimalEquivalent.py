# Program to find the Decimal Equivalent of (1/2,1/3,1/4...,1/10)

for de in range(2,11) :                 # range(n,m) function put value lie between n and m including n also
    print('The Decimal Equivalent of 1/{} is {}'.format(de,1/de))       # .format() put value stored in variable at the
                                                                        # place of {}, the first '{}' replaces value of
                                                                        # first argument inside .format() and so on...