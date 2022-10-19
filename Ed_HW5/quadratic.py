from argparse import ArgumentError
import cmath


class Quadtraic:

    def __init__(self, a, b, c):
        if a == 0:
            raise ArgumentError("A cannot be equal to zero.")
        if type(a) != float or type(b) != float or type(c) != float:
            raise ArgumentError("A, B, C must be real numbers.")
        self.a = a
        self.b = b
        self.c = c
        self.d = (b**2) - (4*a*c)
        self.sol1 = (-b-cmath.sqrt(self.d))/(2*a)
        self.sol2 = (-b+cmath.sqrt(self.d))/(2*a)

    def __repr__(self):
        f'Quadtraic(a={self.a}, b={self.b}, c={self.c})'

    def __str__(self):
        f'Quadtraic(a={self.a}, b={self.b}, c={self.c})'

    def get_discriminant(self):
        return self.d

    def get_roots(self):
        return (self.sol1, self.sol2)
