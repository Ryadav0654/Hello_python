import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumfrence = 2*math.pi*radius
    return area, circumfrence


radius = float(input("enter the radius of circle: "))
a, c = circle_stats(radius)
print("area: ", round(a, 3), " and circumfrence: ", round(c, 3))