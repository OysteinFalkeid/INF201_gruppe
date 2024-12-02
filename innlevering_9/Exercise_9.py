import numpy as np
import pytest
from typing import Union, Optional
import abc

# Task 0
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add_vectors(self, other_vector):
        return self.x + other_vector.x, self.y + other_vector.y
a = Vector2D(1.0, 2.0)
b = Vector2D(3.0, 3.5)
c = a.add_vectors(b)  

#@pytest.mark.parameterize("a,b,c",[Vector2D(1.0,2.0), Vector2D(4.0,4.0), Vector2D(5.0,6.0)])
def test_add_vectors(a, b, c):
    c = a + b
    assert c.x == a.x + b.x
    assert c.y == a.y + b.y

# Task 1
class Complex:
    def __init__(self, re = 0, im = 0):
            self.re = re
            self.im = im

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(self.re + other, self.im)
        else:  
            return Complex(self.re + other.re, self.im + other.im)
    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(other + self.re, self.im)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(self.re - other, self.im)
        else:
            return Complex(self.re - other.re, self.im - other.im)
    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(other - self.re, -self.im)

    def __mul__(self, const):
        if type(const) == int or type(const) == float: 
            return Complex(const * self.re, const * self.im)
        else:
            return Complex(self.re * const.re  - self.im * const.im, self.im * const.re + self.re * const.im)
    def __rmul__(self, const):
        if type(const) == int or type(const) == float: 
            return Complex(self.re * const, self.im * const)
        
    def __truediv__(self, const):
        if type(const) == int or type(const) == float: 
            return Complex(self.re / const, self.im / const)
           
        else:
            return Complex((self.re * const.re + self.im * const.im) / (const.re**2 + const.im**2), (self.im * const.re - self.re * const.im) / (const.re**2 + const.im**2))
    def __rtruediv__(self, const):
        if type(const) == int or type(const) == float: 
             return Complex(const * self.re / (self.re**2 + self.im**2), - const * self.im / (self.re**2 + self.im**2))

    def __conj__(self):
        return Complex(self.re, -self.im)

    def __str__(self):
        if self.im > 0:
            return f"{round(self.re, 4)} + {round(self.im, 4)}i"
        else:
            return f"{round(self.re, 4)} - {round(abs(self.im), 4)}i"
        
class Real:
    def __init__(self, re):
        self.re = re
        self.im = 0

class Immaginary:
    def __init__(self, im):
        self.im = im
        self.re = 0

# a = Complex(-1,2) + 4
# b = Complex(3,2) + Immaginary(2) + Real(2)
# c = Complex() - 2 - Immaginary(2)
# d = a.__conj__()
# e = a - b + c
# f = 2 * a * 3
# g = a / b
# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)
# print('e = ', e)
# print('f = ', f)
# print('g = ', g)