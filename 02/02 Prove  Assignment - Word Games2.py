adjective1 = input("Please enter an adjective: ")
adjective2 = input("Please enter a noun: ")
noun1 = input("Please enter a verb: ")
# check if the noun starts with a vowel
if noun1[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"
adverb = input("Please enter an adverb: ")
verb2 = input("Please enter a verb: ")
noun2 = input("Please enter a noun: ")
if noun2[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"

# Capitalize the adverb
adverb = adverb.capitalize()

# Use f-strings to insert the user's input into the story
story = f"It was a {adjective1} day and I was feeling {adjective2}. I decided to take my {noun1} for a {adverb}. As we were {verb2}ing, I noticed a {noun2} in the distance."

# Print the story
print(story)