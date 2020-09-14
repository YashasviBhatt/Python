def Verify(year, month):
    if year > 1901 and 0 < month < 13:
        pass
    else:
        print('\nInvalid Values Entered\n')
        Main()
        exit()

def GenerateCalender(year, month):
    month_days_dict = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
                       'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31, }

    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        month_days_dict['February'] = 29

    schedule_1901 = {'January':{'Tuesday':[1, 8, 15, 22, 29]}, 'February':{'Friday':[1, 8, 15, 22]},
                            'March':{'Friday':[1, 8, 15, 22, 29]}, 'April':{'Monday':[1, 8, 15, 22, 29]},
                            'May':{'Wednesday':[1, 8, 15, 22, 29]}, 'June':{'Saturday':[1, 8, 15, 22, 29]},
                            'July':{'Monday':[1, 8, 15, 22, 29]}, 'August':{'Thursday':[1, 8, 15, 22, 29]},
                            'September':{'Sunday':[1, 8, 15, 22, 29]}, 'October':{'Tuesday':[1, 8, 15, 22, 29]},
                            'November':{'Friday':[1, 8, 15, 22, 29]}, 'December':{'Sunday':[1, 8, 15, 22, 29]}}

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    for day in days:
        print(day, end='  ')

def Main():
    input_year = int(input('Enter Year (after 1901) : '))
    input_month = int(input('Enter Month : '))

    Verify(input_year, input_month)

    month_name_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                       7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    print('\n{} {}\n'.format(month_name_dict[input_month], input_year))

    GenerateCalender(input_year, input_month)