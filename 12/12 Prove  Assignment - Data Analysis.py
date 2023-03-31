# https://byui-cse.github.io/cse110-course/lesson12/prove.html

# 12 Prove: Assignment - Data Analysis

# Semih Aydin

# prompt the user to enter the year of interest and handle exceptions
while True:
    try:
        year_of_interest = int(input('Enter the year of interest: '))
        if year_of_interest < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a correct number")

# prompt the user to enter the country of interest 
country_of_interest = input('Enter the country of interest: ').lower()

# set initial values for variables
max_life_expectancy = -1
max_entity = ""
max_year = None

min_life_expectancy = 999
min_entity = ""
min_year = None
life_expectancy_list = []

country_max_life_expectancy = 0
country_max_year = None
country_min_life_expectancy = 999
country_min_year = None

# Load the data file 
with open ('life-expectancy.csv') as file:
    next(file) # skip the header row

    # set a flag to check if data is found for the given year and country
    data_found = False

    for line in file:
        clean_line = line.strip() # taking care of whitespace 
        parts = clean_line.split(',') # splitting the lines

        # extract entity, code, year, and life expectancy from each line
        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # find the overall highest and lowest life expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_entity = entity
            max_year = year
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_entity = entity
            min_year = year
        
        # find life expectancy data for the given year
        if year == year_of_interest :
            life_expectancy_list.append(life_expectancy)
            avarage_life_expectancy = sum(life_expectancy_list)/ len(life_expectancy_list)
            chosen_max_life_expectancy = max(life_expectancy_list)
            chosen_max_entity = entity if life_expectancy == chosen_max_life_expectancy else chosen_max_entity
            chosen_min_life_expectancy = min(life_expectancy_list)
            chosen_min_entity = entity if life_expectancy == chosen_min_life_expectancy else chosen_min_entity


        # find the highest and lowest life expectancy for the given country
        if entity.lower() == country_of_interest:
            if country_max_year is None or life_expectancy > country_max_life_expectancy:
                country_max_life_expectancy = life_expectancy
                country_max_year = year
                
            if country_min_year is None or life_expectancy < country_min_life_expectancy:
                country_min_life_expectancy = life_expectancy
                country_min_year = year
            
                # find the life expectancy data for the given year and country
        if entity.lower() == country_of_interest and year == year_of_interest:
            print(f"\nThe life expectancy for {entity} in {year} is {life_expectancy:.2f}")
            data_found = True

    # output message if data is not found for the given year and country
    if not data_found:
        print(f"No data found for {country_of_interest} in {year_of_interest}")


# output results for the overall list 
print('\nOverall for the list :')
print(f'The overall max life expectancy is: {max_life_expectancy:.2f} from {max_entity} in {max_year}')
print(f'The overall min life expectancy is: {min_life_expectancy:.2f} from {min_entity} in {min_year}')

# output results for the given year
print(f'\nFor the year {year_of_interest}:')
print(f'The average life expectancy across all countries was {avarage_life_expectancy:.2f}')
print(f'The max life expectancy was in {chosen_max_entity} with {chosen_max_life_expectancy:.2f}')
print(f'The min life expectancy was in {chosen_min_entity} with {chosen_min_life_expectancy:.2f}')

# output results for the given country
if country_max_year is not None:
    print(f"\nFor {country_of_interest.capitalize()}:")
    print(f"Minimum life expectancy: {country_min_life_expectancy:.2f} in {country_min_year} ")
    print(f"Maximum life expectancy: {country_max_life_expectancy:.2f} in {country_max_year} ")
else:
    print(f"No data found for {country_of_interest}")

print()


