from calendar import month

def GenerateCalender(input_year, input_month):
    if len(str(input_year)) == 4 and 1 <= input_month <= 12:
        print('\n',month(input_year, input_month))
    else:
        print('\nInvalid Details Entered')
        print('Enter Details Again\n')
        Main()

    return True

def Main():
    input_year = int(input('Enter Year : '))
    input_month = int(input('Enter Month Number : '))
    GenerateCalender(input_year, input_month)
    return True

Main()