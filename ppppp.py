class Point ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"the coordinates are: ({self.x}, {self.y})")
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        print(f"the coordinates has been changed into: ({self.x}, {self.y})")
        
a = int(input("Enter x"))
b = int(input("Enter y"))
u = Point(a,b)
u.show()
ar = int(input("change x"))
br = int(input("change y"))

u.move(ar,br)