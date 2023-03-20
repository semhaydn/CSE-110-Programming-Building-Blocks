import random

# list of words to guess
word_list = ["nephi", "lehi", "alma", "helaman", "mormon", "moroni"]

# display the welcome message 
print('Welcome to the word guessing game!')

# set up initial variables
num_guesses = 0
correct_guess = False

while True:
    # choose a random word from the list
    secret_word = random.choice(word_list)
    # reset variables
    num_guesses = 0
    correct_guess = False

    # loop until the user guesses correctly
    while not correct_guess:
        # prompt the user for a guess
        guess = input("What is your guess? ")
        num_guesses += 1 

        # check if the guess is correct
        if guess == secret_word:
            correct_guess = True
            print("Congratulations! You guessed it!")
            print(f"It took you {num_guesses} guesses.")
        else:
            print("Your guess was not correct.")
    
    play_again = input("Do you want to play again? (yes or no) ")
    if play_again.lower() != "yes":
        break
