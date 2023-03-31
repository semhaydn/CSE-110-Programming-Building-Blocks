# first_name = input('Enter your first name: ').upper()
# first_name_initial = first_name[0:1]
# last_name = input('Enter your last name: ').upper()
# last_name_initial = last_name[0:1]

# print(f'Your initials are: {first_name_initial}{last_name_initial}')

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name)

# print(f'Your initials are: {first_name_initial}{last_name_initial}')



def get_initial(name):
    if not name:
        return ''
    initial = name[0].upper()
    return initial

while True:
    first_name = input('Enter your first name: ')
    if first_name.isalpha() and len(first_name) <= 20:
        break
    print('Invalid input. Please enter a valid first name (letters only, max length 20).')
first_name_initial = get_initial(first_name)


while True:
    last_name = input('Enter your last name: ')
    if last_name.isalpha() and len(last_name) <= 20:
        break
    print('Invalid input. Please enter a valid last name (letters only, max length 20).')
last_name_initial = get_initial(last_name)


print(f'Your initials are: {first_name_initial}{last_name_initial}')