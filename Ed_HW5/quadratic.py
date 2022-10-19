from math import sqrt


class Quadtraic:

    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            raise Exception("A cannot be equal to zero.")
        if type(a) != int or type(b) != int or type(c) != int:
            raise TypeError(a, b, c)
        self.a = a
        self.b = b
        self.c = c
        self.d = (b**2) - (4 * a * c)
        try:
            self.sol1 = (-b - sqrt(self.d)) / (2 * a)
        except ValueError:
            raise Exception("Not real root")
        try:
            self.sol2 = (-b + sqrt(self.d)) / (2 * a)
        except ValueError:
            raise Exception("Not real root")
        

    def __repr__(self):
        f'Quadtraic(a={self.a}, b={self.b}, c={self.c})'

    def __str__(self):
        f'Quadtraic(a={self.a}, b={self.b}, c={self.c})'

    def get_discriminant(self):
        return self.d

    def get_roots(self):
        return (self.sol1, self.sol2)
