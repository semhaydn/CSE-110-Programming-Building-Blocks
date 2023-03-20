import math

# Square
side = float(input("What is the length of a side of the square? "))
area_square = side ** 2
print(f"The area of the square is: {area_square}")

# Rectangle
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area_rectangle = length * width
print(f"The area of the rectangle is: {area_rectangle}")

# Circle
radius = float(input("What is the radius of the circle? "))
area_circle = math.pi * radius ** 2
print(f"The area of the circle is: {area_circle}")

# Stretch Challenge 1
# Using math.pi instead of hardcoding the value

# Stretch Challenge 2
# Prompting the user for a single length value and using it to calculate multiple areas and volumes
length = float(input("Enter a length value: "))

# Square
area_square = length ** 2
print(f"The area of the square is: {area_square}")

# Circle
area_circle = math.pi * length ** 2
print(f"The area of the circle is: {area_circle}")

# Cube
volume_cube = length ** 3
print(f"The volume of the cube is: {volume_cube}")

# Sphere
volume_sphere = 4/3 * math.pi * length ** 3
print(f"The volume of the sphere is: {volume_sphere}")

# Stretch Challenge 3
# Prompting the user for the value in centimeters and displaying the area in square centimeters and square meters

# Square
side = float(input("What is the length of a side of the square in centimeters? "))
area_square = side ** 2
area_square_cm = area_square
area_square_m = area_square / (10 ** 4)
print(f"The area of the square is: {area_square_cm} square centimeters or {area_square_m} square meters")

# Rectangle
length = float(input("What is the length of rectangle in centimeters? "))
width = float(input("What is the width of the rectangle in centimeters? "))
area_rectangle = length * width
area_rectangle_cm = area_rectangle
area_rectangle_m = area_rectangle / (10 ** 4)
print(f"The area of the rectangle is: {area_rectangle_cm} square centimeters or {area_rectangle_m} square meters")

# Circle
radius = float(input("What is the radius of the circle in centimeters? "))
area_circle = math.pi * radius ** 2
area_circle_cm = area_circle
area_circle_m = area_circle / (10 ** 4)
print(f"The area of the circle is: {area_circle_cm} square centimeters or {area_circle_m} square meters")