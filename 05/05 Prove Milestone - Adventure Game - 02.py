# Text Adventure Game

print("Welcome to the Text Adventure Game!")

def start():
    print("You find yourself in a dark forest. In front of you, there is a path that splits into two directions.")
    print("Do you go left or right?")
    choice = input("Enter 'left' or 'right': ")

    if choice == "left":
        print("You find yourself in front of a river. There is a raft floating nearby.")
        raft_choice()
    elif choice == "right":
        print("You come across a treacherous cliff. There is a rope hanging over the edge.")
        cliff_choice()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        start()

def raft_choice():
    print("Do you use the raft to cross the river?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("You successfully cross the river and continue your journey.")
    elif choice == "no":
        print("You lose your chance to cross the river and your journey ends here.")
        end()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        raft_choice()

def cliff_choice():
    print("Do you use the rope to climb down the cliff?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("You fall to your death. Your journey has come to an end.")
        end()
    elif choice == "no":
        print("You decide to turn back and find another way. Your journey continues.")
        start()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        cliff_choice()

def end():
    print("Game Over.")

start()