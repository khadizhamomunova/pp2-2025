class rectangle(shape):
    def init(self, length, width):
        super().init()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width