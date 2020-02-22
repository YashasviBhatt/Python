# Python Program to calculate distance between 2 points
# For this we use Euclidean Distance
# This Could have done using either math.sqrt() function to find the square root of the value
# Or Numpy.Euclidean function could have used for this

print('Enter I Coordinate')
x1,y1=int(input('Enter x1 : ')),int(input('Enter y1 : '))
x2,y2=int(input('Enter x2 : ')),int(input('Enter y2 : '))

def Euclidean(x1,y1,x2,y2) :
    return (((y2-y1)**2+(x2-x1)**2)**(1/2))                 # (a)**n finds the nth root of a

d=Euclidean(x1,y1,x2,y2)
print(d)
