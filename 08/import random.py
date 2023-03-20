import random

words = ["france", "sariah", "nephi", "jacob", "mosiah", "alma", "moroni"]

secret_word = random.choice(words)

guess = ""
guess_count = 0
MAX_GUESSES = 10

# generate the initial hint
hint = "_" * len(secret_word)

print("Welcome to the word guessing game!\n")

while guess != secret_word and guess_count < MAX_GUESSES:
    print(f"Your hint is: {hint}")
    guess = input("What is your guess? ").lower()
    
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        guess_count += 1
        continue
    
    guess_count += 1
    new_hint = ""
    
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            new_hint += guess[i].upper()
        elif guess[i] in secret_word:
            new_hint += guess[i].lower()
        else:
            new_hint += "_"
    
    hint = new_hint
    
    if guess == secret_word:
        print(f"Congratulations! You guessed it!\nIt took you {guess_count} guesses.")
        break
    
    if guess_count >= MAX_GUESSES:
        print(f"Sorry, you ran out of guesses. The secret word was {secret_word}.\n")

