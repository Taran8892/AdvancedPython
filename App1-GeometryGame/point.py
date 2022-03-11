class Point():

    def __init__(self, x, y):
        print("point created")
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowerLeft, UpperRight):
        # ((5,6),(7,9))
        if lowerLeft[0] < self.x < UpperRight[0] and lowerLeft[1] < self.y < UpperRight[1]:
            return True
        else:
            return False
    
    def distance_from_point(self, x, y):
        return ((y - self.y)**2 + (x - self.x)**2)**0.5



point1 = Point(6,7)

print(point1.falls_in_rectangle((5,6),(7,9)))
print(point1.distance_from_point(9, 9))
