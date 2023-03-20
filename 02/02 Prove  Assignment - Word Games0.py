# Ask the user for input
adjective = input("Please enter an adjective: ")
animal = input("Please enter an animal: ")
verb1 = input("Please enter a verb: ")
exclamation = input("Please enter an exclamation: ")
verb2 = input("Please enter another verb: ")
verb3 = input("Please enter a final verb: ")
noun1 = input("Please enter a noun: ")
adverb = input("Please enter an adverb: ")
noun2 = input("Please enter a noun: ")

# Capitalize the exclamation and adverb
exclamation = exclamation.capitalize()
adverb = adverb.capitalize()

# check if the noun starts with a vowel
if noun2[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"

    # check if the noun starts with a vowel
if noun1[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"

# Use f-strings to insert the user's input into the story
story = f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. I felt so relieved and  decided to take {noun1} and went for a {adverb} walk. On my way, I saw {article} {noun2}."

# Print the story
print(story)