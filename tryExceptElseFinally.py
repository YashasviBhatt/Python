try:
    inpt = int(input('Enter any Year : '))
except:
    print('Wrong Input! Year is an Integer')
else:
    if len(str(inpt)) == 4:
        print('Correct Input! You Wisdom will be Saluted')
    else:
        print('Wrong Input!')
finally:
    print('Your Program Executed Completely')