import math

class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Точка: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt()