#2 Create proper member variables inside the task if required and use them when necessary.For example for this task
# create a class private variable named pi=3.141
class Circle:

    # class variable
    pi = 3.14

    # constructor
    def __init__(self, radius):
        self.radius = radius

    # instance method
    def area_of_circle(self):
        area = self.pi * self.radius * self.radius
        return area

    # instance method
    def perimeter_of_circle(self):
        perimeter = 2 * self.pi * self.radius
        return perimeter
   
    def display_pi(self):
        return self.pi


if __name__ == "__main__":    
    # object of the class Circle
    c = Circle(10)

    print("Area of Circle : ", c.area_of_circle())

    print("Perimeter of Circle : ", c.perimeter_of_circle())

    print("Value of pi : ", c.display_pi())
