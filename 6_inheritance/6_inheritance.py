class rectangle():
    def __init__(rect,l,b):
        rect.length=l
        rect.breadth=b
    def display(rect):
        print("\nLength and breadth of rectangle is ",rect.length,rect.breadth)
    def area(rect):
        area=rect.length*rect.breadth
        print("area = ",area)

class rectangles(rectangle):
    pass
a=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
x= rectangles(a,b)
x.display()
x.area()

