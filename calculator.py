#Program for Calculator using if

num1=0
num2=0
c=0
ans=0

print("Welcome")
num1=input("Enter First Number\n")
num2=input("Enter Second Number\n")
c=input("Enter \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nSo Your Coice is\n")

if num1==0 and num2==0 and c==0 :
    print("Values Not Entered Properly")
else :
    if c==1 :
        ans=num1+num2
    elif c==2 :
        ans=num1-num2
    elif c==3 :
        ans=num1*num2
    else :
        ans=int(num1)/int(num2)

print("So the Answer after chosen operation is : ",ans)