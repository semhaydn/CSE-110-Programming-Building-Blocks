# https://byui-cse.github.io/cse110-course/lesson13/checkpoint.html

# 13 Prepare: Checkpoint

# Semih Aydin

def display_regular():
    print(message)
    
    

def display_uppercase():
    print(message.upper())

def display_lowercase():
    print(message.lower())


    
while True:
    message = input('What is your message? ')
    if len(message) <= 50: 
        break
    print('Invalid input. Please enter a valid message (max length 50).')


display_regular()
display_uppercase()
display_lowercase()


