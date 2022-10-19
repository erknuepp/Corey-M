import cylinder
from quadratic import Quadtraic

q = cylinder.Cylinder(3, 4)

# print(q.calculate_volume())

q1 = Quadtraic(5, -10, 5)  # real roots
print(q1.get_roots())

q2 = Quadtraic(1, -1, 0)  # identical roots
print(q2.get_roots())

q3 = Quadtraic(3, 4, 5)  # no real roots
print(q3.get_roots())
