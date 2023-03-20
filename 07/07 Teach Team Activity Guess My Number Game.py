import random

# using a while loop to repeat the game as long as the user answers 'yes'
play_again = 'yes'

while play_again == 'yes':
    number = random.randint(1, 100) # generating a random magic number
    num_guesses = 0
    print()
    print('What is the magic number? ')

    guess = None

    # entering a loop
    while guess != number:
        guess = int(input('What is your guess? '))
        num_guesses += 1

        if guess > number:
            print('Lower')
        else:
            print('Higher')

    # displaying a congrats
    print('You guessed it!')

    # displaying numbers of guesses the user has made
    print(f"You took {num_guesses} guesses.")

    # asking user if he/she wants to play again
    play_again = input("Do you want to play again? (yes/no) ")
