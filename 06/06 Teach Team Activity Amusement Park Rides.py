# 06 Teach: Team Activity Amusement Park Rides

# Welcoming the guest

# print('Welcome to Newark Amusement park! ')
# print('We are here to help you! ')

# CORE REQUIREMENTS
def ride_decision():
    first_rider_age = int(input('What is the age of the first rider? '))
    first_rider_height = float(input('What is the height of the first rider? '))
    second_rider = input('Is there a second rider (yes/no)? ')
    second_rider.lower()
    if second_rider == 'yes':
        second_rider_age = int(input('What is the age of the second rider? '))
        second_rider_height = int(input('What is the height of the second rider? '))
    
        if second_rider_height > 35:
            decision = True
        elif second_rider_age > 17 or first_rider_age > 17:
            decision = True
        else:
            decision = False
    else:
        if first_rider_height > 35:
            decision = True
        if first_rider_height > 61 and first_rider_age > 17:
            decision = True
        else:
            decision = False
    return decision


# Display the decision
result = ride_decision()
if result:
    print('Welcome to the ride. Please be safe and have fun! ')
else:
    print('Sorry, you may not ride. ')