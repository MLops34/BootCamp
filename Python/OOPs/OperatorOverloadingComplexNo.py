class Complex:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)
    

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag


    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(3, 4)
c2 = Complex(5, 6)

c3 = c1 + c2

print("Sum:", c3)

c4 = Complex(8, 10)

print("Are equal:", c3 == c4)
