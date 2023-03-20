# 08 Prove: Assignment Wordle 

import random

# Define a list of possible secret words
words = ['france', 'italy', 'germany', 'brasil', 'russia', 'spain', 'china']

# Choose a random word from the list
secret_word = random.choice(words)

# Create a list to hold the current guess
current_guess = ['_'] * len(secret_word)

# Initialize the number of guesses made
num_guesses = 0

# Greet the user and explain the game
print("Welcome to the Word Guessing Game!\n")
print("I've chosen a secret word. Your job is to guess the word by suggesting a word one letter at a time.")
print(f"The word I'm thinking of has {len(secret_word)} letters.\n")

# Start the game loop
while True:
    # Display the current state of the guess
    print(f"Current Guess: {' '.join(current_guess)}\n")
    
    # Get the user's guess and convert it to lowercase
    guess = input("Enter your guess (or type 'exit' to quit): ").lower()

    # Check if the user wants to quit
    if guess == 'exit':
        print("Thanks for playing! Goodbye!")
        break

    # Check if the guess is the same length as the secret word
    if len(guess) != len(secret_word):
        print("Sorry, your guess must have the same number of letters as the secret word.\n")
        continue

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == secret_word:
        print(f"\nCongratulations! You guessed the word in {num_guesses} guesses!")
        break

    # Otherwise, generate a hint
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append('_')
    hint_str = ' '.join(hint)

    # Display the hint
    print(f"\nHint: {hint_str}\n")
