# #Square
side = float(input("what is the  lenght of a side of the square? :"))
area_square = side * side
print(f"The lenght of the square is : {area_square}")

# #Rectangle
lenght = float(input("What is the lenght of rectangle? :"))
width = float(input("What is the width of the rectangle? :"))
area_rectangle = lenght * width
print(f"The are of the rectangle is : {area_rectangle}")

# #Circle
radius = float(input("What is the radius of the circle? :"))
area_circle = (radius * radius) * 3.14
print(f"The area of the circle is : {area_circle}")

# Stretch challenge1
import math
radius = float(input("What is the radius of the circle? :"))
area_circle = (radius * radius) * math.pi
print(f"The area of the circle is : {area_circle}")

# Stretch challenge
value = float(input("What is the value to be used ? :"))

#Square
area_square = value ** 2
print(f"The area of the square is : {area_square} ")

# Circle
area_circle = (value ** 2) * math.pi
print(f"The area of the circle is : {area_circle}")

#Cube
volume_cube = (value ** 3)
print(f"The volume of the cube is {volume_cube}")

#Sphere
volume_sphere = (4/3) * math.pi * (value ** 3)
print(f"The volume of the sphere is : {volume_sphere}")



