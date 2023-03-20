# https://byui-cse.github.io/cse110-course/lesson11/teach.html

# 11 Teach: Team Activity
# Human Resources System

# Semih Aydin 

# OPENING THE FILE
with open('hr_system.txt') as hr_file:
    for line in hr_file:
        # taking care of white spaces 
        # Splitting the lines
        parts = line.split(' ')
        # identifying names and titles
        name = parts[0]
        id_number = parts[1]
        title = parts[2]

        # calculating the salary, paycheck and the bonuses
        salary = float(parts[3])

        if title == 'Engineer':
            pay_check = (salary/24)+1000
        
        else:
            pay_check = (salary/24)
        
        # Displaying names and titles to user
        print(f'{name} (ID: {id_number}), {title} - $ {pay_check:.2f}')