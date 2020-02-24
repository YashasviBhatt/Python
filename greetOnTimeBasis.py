# Program to Greet a Person on the basis of time


import datetime as dt
dayhr=dt.datetime.now().hour

if dayhr < 12 :
    print("Good Morning")
elif dayhr > 12 and dayhr < 16 :
    print("Good Afternoon")
elif dayhr > 16 and dayhr < 20 :
    print("Good Evening")
else :
    print("Good Night")
