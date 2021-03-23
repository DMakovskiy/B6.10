class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rect_str(self):
        return 'Rectangle (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.width) + ', ' + str(self.height) + ')'

a = Rectangle(5, 10, 50, 100)

print(a.rect_str())
print(type(a.rect_str()))
