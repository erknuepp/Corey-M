#%%
from math import sqrt

class quadratic_formula:
    #Inputs to the quadratic formula
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    #Dont really understand repr and str
    def __repr__(self) -> str:
        return "Quadratic_Formula(%d,%d,%d)" % (self.a,self.b,self.c)

    def __str__(self) -> str:
        return "(%d,%d,%d)" % (self.a,self.b,self.c)

    #Calculates the discriminant
    def discriminant(self):
        return self.b**2-4*self.a*self.c
         
    #Calculates the roots
    def roots(self):
        x1 = -self.b + sqrt(self.b**2-4*self.a*self.c) // 2*self.a
        x2 = -self.b - sqrt(self.b**2-4*self.a*self.c) // 2*self.a
        return (x1,x2)

#%%
# #Other creat sub classes?
# class discriminant(quadratic_formula):
#     def discriminant(self):
#         discriminant = self.b**2-4*self.a*self.c
#         return discriminant
