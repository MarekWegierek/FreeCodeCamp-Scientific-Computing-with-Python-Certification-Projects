class Rectangle:

    def __init__(self, width=0, height=0):    
        self.width = width
        self.height = height
        

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        result = ''
        if self.height >=50 or self.width >=50:
            result = 'Too big for picture.'
        else:
            for i in range(self.height):
                result += self.width*'*' + '\n'
        return result

    def get_amount_inside(self, shape):
        result = 0
        if self.width < shape.width or self.height < shape.height:
            result = 0
        else:
            result = (self.width//shape.width) * (self.height//shape.height)
        return result 

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.height})'
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.height = height
        self.width = height

    def set_side(self, side):
        self.width = side
        self.height = side
