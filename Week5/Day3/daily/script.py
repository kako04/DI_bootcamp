import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified.")
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius

c1 = Circle(radius=5)
c2 = Circle(diameter=10)

print(c1.radius)  
print(c2.diameter) 

print(c1.area()) 

print(c2) 

c3 = c1 + c2
print(c3.radius) 

print(c1 == c2) 
print(c1 > c2)  

circles = [c1, c2, c3]
circles.sort()
print(circles) 
