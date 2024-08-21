# FreeCodeCamp Certification Project 4 (of 5)
# Scientific Computing With Python (Beta)
# Completed 8/21/2024

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        rows = self.height
        cols = self.width
        output = ''
        for i in range(rows):
            output += '*' * cols + '\n'
        
        return output
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side_length):
        self.width = side_length

    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_height(self, side_length):
        self.height = side_length
        self.width = side_length

    def get_picture(self):
        if self.width > 50:  
            return 'Too big for picture.'
        
        output = ('*' * self.width + '\n') * self.width  
        return output

r1 = Rectangle(5, 5)
s1 = Square(10)
print(s1)
print(s1)
print(s1.get_area())
print(r1)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_amount_inside(s1))
print(s1.get_picture())