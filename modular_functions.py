import math

def area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return (1/2) * dimension1 * dimension2
    else:
        raise ValueError("Invalid shape")

print("Area of circle with radius 9 is:", area("circle", 9))
print("Area of rectangle with length 21 and width 6 is:", area("rectangle", 21, 6))
print("Area of triangle with base 6 and height 14 is:", area("triangle", 6, 14))

