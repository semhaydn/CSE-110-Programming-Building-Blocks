# https://byui-cse.github.io/cse110-course/lesson11/prove.html

# 11 Prove: Assignment Milestone

# Semih Aydin 

# Load the data file 

with open ('life-expectancy.csv') as file:
    next(file) # skip the header row

    # create an empty list to store values 
    life_expectancies = [] 
    years = []

    for line in file:
        clean_line = line.strip() # taking care of whitespace 
        parts = clean_line.split(',') # splitting the lines

        # identifying the entity and code values
        entity = parts[0]
        code = parts[1]

        # identifying the year value from the cvs file
        year = int(parts[2])
        # adding each year value to the '' years '' list that we created above
        years.append(year)

        # identifying the life expectancy value from the cvs file
        life_expectancy = float(parts[3])
        # adding each life expectancy value to the '' life expectancies '' list that we created above
        life_expectancies.append(life_expectancy)


    # finding the max values for both list that we created
    life_expectancy_max = max(life_expectancies)
    life_expectancy_low = min(life_expectancies)
    
    # displaying that to the user
    print(f'Highest value is { life_expectancy_max:.2f}')
    print(f'Lowest value is : {life_expectancy_low:.2f}')