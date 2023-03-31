# https://byui-cse.github.io/cse110-course/lesson13/teach.html

# 13 Teach: Team Activity

# Semih Aydin

import math

def compute_area(choice, side=0, radius=0, length=0, width=0):
    area = -1
    
    if choice == "square":
        if side <= 0:
            print("Invalid side length. Please enter a positive value.")
        else:
            area = side * side
    elif choice == "circle":
        if radius <= 0:
            print("Invalid radius. Please enter a positive value.")
        else:
            area = math.pi * radius ** 2
    elif choice == "rectangle":
        if length <= 0 or width <= 0:
            print("Invalid length or width. Please enter positive values.")
        else:
            area = length * width   
    return area
# Prompting a welcome
    # Asking for the choice
while True:
    choice = input('What kind of shape do you have? (square, rectangle, circle or quit if you want to quit): ').lower()
    if choice == 'quit':
        break
    elif choice == '':
        print('Please enter a shape name.')
        continue
    # prompting user result for square
    elif choice == 'square':
        while True:
            try:
                side = float(input("What is the length of a side of the square? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        area_square = compute_area(choice, side)
        if area_square >= 0:
            print(f'The area of the square is {area_square}')
    # prompting user result for rectangle
    elif choice == 'rectangle':
        while True:
            try:
                length = float(input("What is the length of the rectangle? "))
                width = float(input("What is the width of the rectangle? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        area_rectangle = compute_area(choice, length=length, width=width)
        if area_rectangle >= 0:
            print(f'The area of the rectangle is {area_rectangle}')
    # prompting user result for circle
    elif choice == 'circle':
        while True:
            try:
                radius = float(input("What is the radius of the circle? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        area_circle = compute_area(choice, radius=radius)
        if area_circle >= 0:
            print(f'The area of the circle is {area_circle:.2f}')     
    else:
        print('Invalid shape name. Please enter a valid name (square, rectangle, circle, quit).')






    