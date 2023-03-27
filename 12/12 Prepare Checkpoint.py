#  https://byui-cse.github.io/cse110-course/lesson12/checkpoint.html

# 12 Prepare: Checkpoint

# Semih Aydin 

# Creating the list

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 999
youngest_name = ""

# Entering the loop
for line in people:

    # cleaning the lines and seperating the items
    line = line.strip()
    parts = line.split(' ')

    # identifying the name and ages
    name = parts[0]
    age = int(parts[1])

    if age < youngest:
        # This is new youngest
        youngest = age

        youngest_name = name

print(f'The youngest person in the list is {youngest_name}, with an age of {youngest}.')
    
