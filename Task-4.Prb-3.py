'''
Problem 3: From the given list create two class methods area and perimeter which will be going to calculate the area and perimeter.
'''

class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2*3.14*self.radius
obj = Circle(3)
print("Area of circle:",obj.area())
print("Perimeter of circle:",obj.perimeter())