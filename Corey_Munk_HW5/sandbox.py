
#%%
from quadratic import quadratic_formula


calc = quadratic_formula(1,-1,0)

#Print result for disciminant
discriminant = calc.discriminant()
print(discriminant)

#Print result for roots
try:
    roots = calc.roots()
    print(roots)
except:
    print("math domain error")


#%%
from math import sqrt

a,b,c = 1,-1,0

discrim = b**2 - 4*a*c

def roots(a,b,c):
        x1 = -b + sqrt(discrim) // 2*a
        x2 = -b - sqrt(discrim) // 2*a
        return (x1,x2)

print(discrim)

try:
    print(roots(a,b,c))
except:
    print("math domain error")