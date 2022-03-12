from pkgutil import read_code
from random import randint
import turtle

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

class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

class Rectangle():

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def area(self, area):
        if area == (((self.upright.y - self.lowleft.y)**2)**0.5) * (((self.upright.x - self.lowleft.x)**2)**0.5):
            return "Correct"
        else:
            return "Wrong!! The correct area is ", (((self.upright.y - self.lowleft.y)**2)**0.5) * (((self.upright.x - self.lowleft.x)**2)**0.5)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)


rectangle = GuiRectangle(Point(randint(0,400), randint(0,400)), Point(randint(10,400), randint(10,400)))

print("Rectangle Coordinates: ", rectangle.lowleft.x, rectangle.lowleft.y, "and", rectangle.upright.x,rectangle.upright.y )

user_input = GuiPoint(int(input("Guess X: ")), int(input("Guess Y: ")))

print("Your point was inside rectangle: ", user_input.falls_in_rectangle(rectangle))

user_area = int(input("Calculate the area: "))
print(rectangle.area(user_area))

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_input.draw(myturtle)

turtle.done()

