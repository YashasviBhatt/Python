# Python program to find the year when a person turn 95

import datetime

name=input('Enter Name')
age=int(input('Enter Age'))
now=datetime.datetime.now().year
tage=(95-age)+now
print('Year when you turn 95',tage)
