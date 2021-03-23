class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rect_discribe(self):
        print('Внемли, человече, се есть прямоугольник')
        print('Ширина его', self.width)
        print('Высота его', self.height)


rect1 = Rectangle(10, 5)
rect1.rect_discribe()
