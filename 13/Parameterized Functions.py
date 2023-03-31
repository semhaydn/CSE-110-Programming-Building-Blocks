def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
firs_name_initial = get_initial(force_uppercase = True, name=first_name )

print(f'Your initial is: {firs_name_initial}')
