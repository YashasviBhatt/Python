import time

countdwn=int(input("Enter Countdown Limit : "))

while countdwn >= 0 :
    print(countdwn)
    countdwn=countdwn-1
    time.sleep(1)                   # sleep(n) to give delay of n seconds