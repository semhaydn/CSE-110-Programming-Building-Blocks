# 05 Teach: Team Activity Grade Calculator

# Getting the user input and delivering the letter grade based on the score

grade = float(input('What is your grade percent? (Please enter a value between 0- 100): '))
if grade >= 93:
        letter = 'A'
elif grade < 93 and grade >= 90:
    letter = 'A-'
elif grade < 90 and grade >= 87:
    letter = 'B+' 
elif grade < 87 and grade >= 83:
    letter = 'B'
elif grade < 83 and grade >= 80:
    letter = 'B-'
elif grade < 80 and grade >= 77:
    letter = 'C+'
elif grade < 77 and grade >= 73:
    letter = 'C'
elif grade < 73 and grade >= 70:
    letter = 'C-'
elif grade < 70 and grade >= 67:
    letter = 'D+'
elif grade < 67 and grade >= 63:
    letter = 'D'
elif grade < 63 and grade >= 60:
    letter = 'D-'
elif grade >= 60:
        letter = 'D'
else:
        letter = 'F'

# Displaying the letter grade based on grade percentage
if letter:
    print(f'Your grade is : {letter}')



if grade >= 60:
    print('Congratulation you have passed the class! ')    
else:
    print('Unfortunately you couldnt pass the class. Keep working hard please! ')