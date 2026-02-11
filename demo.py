"""
Bu modül daire alanı hesaplamak için kullanılır.
"""
import math

def circle_area(radius):
    """Returns the area of the circle of given radius. Returns 0 if radius is negative."""
    if radius < 0:
        return 0
    return math.pi * (radius ** 2)