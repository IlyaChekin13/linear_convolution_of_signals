from math import sqrt
from re import A


class ComplexNum(object):
    """Represent imaginary number for my case\n
       Include the real and the imaginary value""" 
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.imag > 0:
            if self.imag != 1:
                return f"{self.real} + {self.imag}i"
            else:
                return f"{self.real} + i"
        elif self.imag < 0:
            if self.imag != -1:
                return f"{self.real} - {-self.imag}i"
            else:
                return f"{self.real} - i"
        else:
            return f"{self.real}"

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.real + other.real, self.imag + other.imag)    
        else:
            return ComplexNum(self.real + other, self.imag)

    def __radd__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.real + other.real, self.imag + other.imag)
        else:
            return ComplexNum(self.real + other, self.imag)

    def __sub__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.real - other.real, self.imag - other.imag)
        else:
            return ComplexNum(self.real - other, self.imag)
    
    def __rsub__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(other.real - self.real, other.imag - self.imag)
        else:
            return ComplexNum(other - self.real, -self.imag)

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))
        else:
            return ComplexNum(self.real * other, self.imag * other)

    def __rmul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum((other.real * self.real) - (other.imag * self.imag),
            (other.imag * self.real) + (other.real * self.imag))
        else:
            return ComplexNum(other * self.real, other * self.imag)

    def __truediv__(self, other):
        if isinstance(other, ComplexNum):
            r = (other.real**2 + other.imag**2)
            return ComplexNum((self.real*other.real - self.imag*other.imag)/r,
                              (self.imag*other.real + self.real*other.imag)/r) 
        else:
            return ComplexNum(self.real / other, self.imag / other)

    def __rtruediv__(self, other):
        if isinstance(self, ComplexNum):
            r = (other.real**2 + other.imag**2)
            return ComplexNum((other.real*self.real - other.imag*self.imag)/r,
                              (other.imag*self.real + other.real*self.imag)/r)
        else:
            r = (self.real ** 2 + self.other ** 2)
            return ComplexNum((other * self.real) / r,
                              (other * self.imag) / r)

    def __abs__(self):
        new = (self.real**2 + (self.imag**2)*-1)
        return ComplexNum(sqrt(abs(new)))       


a = ComplexNum(2, 3)

print(abs(a))