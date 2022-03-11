from pkgutil import read_code
from random import randint

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        # ((5,6),(7,9))
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

class Rectangle():

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def area(self, area):
        if area == (((self.upright.y - self.lowleft.y)**2)**0.5) * (((self.upright.x - self.lowleft.x)**2)**0.5):
            return "Correct"
        else:
            return f"Wrong!! The correct area is {(((self.upright.y - self.lowleft.y)**2)**0.5) * (((self.upright.x - self.lowleft.x)**2)**0.5)}"


rectangle = Rectangle(Point(randint(0,9), randint(0,9)), Point(randint(10,19), randint(10,19)))

print("Rectangle Coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and", rectangle.upright.x, ",",rectangle.upright.y )

user_input = Point(int(input("Guess X: ")), int(input("Guess Y: ")))

print("Your point was inside rectangle: ", user_input.falls_in_rectangle(rectangle))

user_area = int(input("Calculate the area: "))
print(rectangle.area(user_area))

