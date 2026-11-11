import math
def calculate_volume_of_a_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * (radius ** 3)

radius1 = 30
volume1 = calculate_volume_of_a_sphere(radius1)
print(f"The volume of a sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_a_sphere(radius2)
print(f"The volume of a sphere with radius {radius2} is: {volume2}")

