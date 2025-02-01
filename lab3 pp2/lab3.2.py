class Shape:
    def init(self):
        self.length = 0

    def area(self):
        return 0

class Square(Shape):
    def init(self, length):
        super().init()
        self.length = length

    def area(self):
        return self.length ** 2
