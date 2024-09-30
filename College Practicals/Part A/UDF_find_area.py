import math

def rectange_area(length,width):
    return length*width
def square_area(side):
    return side*side
def circle_area(radius):
    return math.pi*(radius**2)
def triangle_area(base,height):
    return 0.5*base*height

shape = input("Enter the shape [rectangle, square, circle, triangle] : ")
display = True

if shape == 'rectangle':
    length = float(input("Enter length : "))
    width = float(input("Enter width : "))
    area = rectange_area(length,width)
elif shape == 'square':
    side = float(input("Enter side : "))
    area = square_area(side)
elif shape == 'circle':
    radius = float(input("Enter radius : "))
    area = circle_area(radius)
elif shape == 'triangle':
    base = float(input("Enter base : "))
    height = float(input("Enter height : "))
    area = triangle_area(base,height)
else:
    print("Invalid shape!")
    display = False

if display == True:
    print(f"Area of {shape} is {area: .2f}")