# Program to store values from a list to an another list which are greater than 5


list=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]

for j in list :
    if j > 5 :
        list1.append(j)
    else :
        list2.append(j)


print("The list of integers which are greater than 5 are",list1)
print("The list of integers which are smaller than 5 are",list2)