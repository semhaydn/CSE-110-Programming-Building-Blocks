import random

color_options = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]

favorite_color = input("If you were a fruit, what color would you be? ")

if favorite_color.lower() in color_options:
  print("That's a great choice! You're as colorful as a rainbow.")
else:
  print("Haha, I don't think that's a real color! Maybe you're a mysterious fruit from outer space.")
