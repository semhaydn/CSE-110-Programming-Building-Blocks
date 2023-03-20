# 04 Teach: Team Activity Speed of a Falling Object

import math 

print('Welcome to the velocity calculator. Please enter the following:')

# Mass in kg
m = float(input('Mass (in kg):'))

# Gravity
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter):'))

# Time
t = float(input('Time (in seconds):'))

# Here we would like to get the info for p , A and C in order to find the "c"
# Density of fluid
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):'))

# Area of the item
A = float(input('Cross sectional area (in m^2):'))

# Drag Constant
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder):'))

# Compute the value of c
c = (1/2*p)*A*C

#blank line
print('')

# Display the value of c
print(f'The inner value of c is:{c:.3f}')


# Compute the overall velocity
velocity_at_t = math.sqrt((m*g)/c) * (1-math.exp((-math.sqrt(m*g*c)/m)*t))

# Display the overall velocity
print(f'The velocity after 10.0 seconds is: {velocity_at_t:.3f}')
