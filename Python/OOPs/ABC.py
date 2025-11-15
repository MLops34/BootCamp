from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

# shape = Shape()        ❌ Error: Can't instantiate abstract class
circle = Circle(5)       # ✅ Works
print(circle.area())     # Output: 78.5
