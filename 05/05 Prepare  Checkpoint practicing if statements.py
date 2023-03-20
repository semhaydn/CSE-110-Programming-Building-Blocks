# 05 Prepare: Checkpoint 

# First question    
first_number = float(input('What is the first number? '))
second_number = float(input('What is the second number? '))

# first condition
if first_number > second_number:
    print('The first number is greater')
    print('The numbers are not equal')
    print('The second number is not greater')

# second condition
elif first_number == second_number:
    print('The first number is not greater')
    print('The numbers are equal')
    print('The second number is not greater')

# third condition
elif first_number < second_number:
    print('The first number is not greater')
    print('The numbers are not equal')
    print('Then second number is greater')

# leaving blank space
print("")


# Second question

favorite_animal = input('What is your favorite animal? ')

# first condition
if favorite_animal.lower() == 'bear':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')
