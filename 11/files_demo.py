# courses_file = open('courses.txt')


with open('courses.txt') as courses_file:
    for line in courses_file:
        line = line.strip()
        parts = line.split(',')
    
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f'{name} - Grade : {grade}, after bonus : {bonus_grade}')

    print()
    print('Goodbye')

print('The file is closed now.')