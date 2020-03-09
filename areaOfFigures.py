class Area :
    def Square(self, side) :
        return side**2
    def Rectangle(self, length, breadth) :
        return length*breadth
    def Circle(self, radius) :
        return 3.14*(radius**2)
    def Triangle(self, base, height):
        return 0.5*base*height

choice=int(input('Enter\n1. Area of Square\n2. Area of Rectangle\n3. Area of Circle\n4. Area of Triangle\n0. Exit\n'))
area=Area()

if choice == 0 :
    exit()

elif choice == 1 :
    side = int(input('Enter Dimension of Sides of Square : '))
    ar = area.Square(side)
    print('The Area of Square is',end=' ')

elif choice == 2 :
    length = int(input('Enter Dimension of Length of Rectangle : '))
    breadth = int(input('Enter Dimension of Breadth of Rectangle : '))
    ar = area.Rectangle(length, breadth)
    print('The Area of Rectangle is',end=' ')

elif choice == 3 :
    radius = int(input('Enter Dimension of Radius of Circle : '))
    ar = area.Circle(radius)
    print('The Area of Circle is', end=' ')

elif choice == 4 :
    base = int(input('Enter Dimension of Base of Triangle : '))
    height = int(input('Enter Dimension of Height of Triangle : '))
    ar = area.Triangle(base, height)
    print('The Area of Triangle is', end=' ')

else :
    print('Invalid Choice Entered')

print(ar)