# A STUDENT MAKES HONOUR ROLL IF THEIR AVARAGE IS >=85
# AND THEIR LOWEST GRADE IS NOT BELOW 75

# I check to see if the requirements for honour roll are met
gpa = float(input('What was your Grade Point Avarage? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 85 and lowest_grade >= 70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if  you need to check if students is 
# on honour

if honour_roll:
    print('You made honour roll')
else:
    print("Keep it up the good work!")