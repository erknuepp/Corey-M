class Cylinder:

    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        return Cylinder.pi * self.radius**2 * self.height

    def calculate_surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.radius + self.height)

    def set_height(self, height):
        self.height = height

    def __str__(self):
        f'Cylinder(radius={self.radius}, height={self.height})'
