# first_name = input('Enter your first name: ').upper()
# first_name_initial = first_name[0:1]
# last_name = input('Enter your last name: ').upper()
# last_name_initial = last_name[0:1]

# print(f'Your initials are: {first_name_initial}{last_name_initial}')

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print(f'Your initials are: {first_name_initial}{last_name_initial}')