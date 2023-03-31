# https://byui-cse.github.io/cse110-course/lesson13/prove.html

# 13 Prove: Assignment Wind Chill Calculations

# Semih Aydin

# Calculates and returns the wind chill based on a given temperature and wind speed.
def calculate(wind_speed=5, temp= 0,):
        windchill = (35.74 + (0.6215* temp) - (35.75*(wind_speed**0.16))+ ((0.4275*temp)*(wind_speed**0.16)))
        return windchill
# Converts a temperature in Celsius to Fahrenheit.
def calculate_degree(temp):
    temp_f = (temp *(9/5) + 32 )
    return temp_f

# Ask user for temperature and unit of measurement
while True:
    print('Welcome to the windchill calculator!')
    try:
        temp = int(input('What is the temperature '))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    choice = input('Fahrenheit or Celcius (F/C) or quit ? ').lower()
    if choice == 'quit':
        break
    elif choice == '':
        print('Please enter a "F" or "C" .')
        continue
    elif choice =='f':
        for wind_speed in range(5, 65, 5):
            windchill = calculate(wind_speed,temp)
            print(f'At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F')
        break
    # Convert temperature to Fahrenheit if necessary
    elif choice =='c':
        temp = calculate_degree(temp)

        # Loop through wind speeds from 5 to 60 mph, incrementing by 5
        for wind_speed in range(5, 65, 5):
            windchill = calculate(wind_speed,temp)
            print(f'At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F')
        break
    else:
        ('Invalid input, please enter a correct input')

    



