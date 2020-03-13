# Program to verify pin
# The Correct Pin for this program is 2014

import time

pin_inputs=[]

for inpt in range(0,3) :
    i=int(input("Enter your Pin : "))
    pin_inputs.append(inpt)
    if i==2014 :
        print("Correct Pin")
        time.sleep(3)
        break
    elif len(pin_inputs) == 3 :
        print("You have Entered wrong Pin 3 times your card has been blocked")
        time.sleep(3)
    else :
        continue
