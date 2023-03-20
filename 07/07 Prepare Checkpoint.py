# 07 Prepare: Checkpoint 

# Asking user for a number
number = int(input('Please type a positive number: '))

# entering to the loop if the number is negative.
while number < 0:
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Please type a positive number: '))

# displaying the number
print(f'The number is: {number}')


# asking the question
candy = input('May I have a pice of candy? ')

# enterin the loop if the answer is not yes
while candy != "yes":
    candy = input('May I have a pice of candy? ')

# displaying a response
print('Thank you.')