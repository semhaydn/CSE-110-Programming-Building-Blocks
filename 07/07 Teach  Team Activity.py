import random

# Print a welcome message to the user
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Using a while loop to repeat the game as long as the user answers 'yes'
play_again = 'yes'

while play_again == 'yes':
    # generating a random magic number
    number = random.randint(1, 100)
    num_guesses = 0

    print('Try to guess the number!')

    guess = int(input('Enter your guess: '))

    # entering a loop
    while guess != number:
        num_guesses += 1

        if guess > number:
            print('Lower')
        else:
            print('Higher')

        guess = int(input('Enter your guess: '))

    # displaying a congratulations message
    print('Congratulations, you guessed it!')

    # displaying number of guesses the user has made
    print(f"You took {num_guesses} guesses.")

    # asking user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")

# Print a goodbye message to the user
print("Thanks for playing the number guessing game! Goodbye!")