print("\nWelcome to Aiden's Adventure!")

print("\nChapter 1:")
print("\nIntroduction: Aiden finds themselves in a forest, where they meet Gandalf and Saron.")

print("\nForest: Aiden must navigate the forest, gathering supplies and avoiding traps.")
while True:
    print("\nWhat would you like to do in the forest?")
    print("climb - Climb a tree")
    print("pick up - Pick up a rock")
    print("fish - Fish for food")
    print("leave - Leave the forest")

    choice = input("Enter your choice: ").lower()
    if choice == "climb":
        print("You climb a tree and gather some supplies.")
    elif choice == "pick up":
        print("You pick up a rock and add it to your collection.")
    elif choice == "fish":
        print("You fish for food and find a delicious meal.")
    elif choice == "leave":
        print("You leave the forest and head towards the castle.")
        break

print("\nCastle: Aiden must help Isabella escape from a castle controlled by Drago.")
while True:
    print("\nWhat would you like to do in the castle?")
    print("unlock - Unlock a door")
    print("break - Break a window")
    print("take - Take some treasure")
    print("leave - Leave the castle")

    choice = input("Enter your choice: ").lower()
    if choice == "unlock":
        print("You unlock a door and help Isabella escape the castle.")
    elif choice == "break":
        print("You break a window and escape the castle.")
    elif choice == "take":
        print("You take some treasure and add it to your collection.")
    elif choice == "leave":
        print("You leave the castle and head towards the battlefield.")
        break

print("\nChapter 2:")
print("\nBattlefield: Aiden must choose whether to ally with Lancelot and his army or to go it alone.")
while True:
    print("\nWhat would you like to do on the battlefield?")
    print("ally - Ally with Lancelot and his army")
    print("go alone - Go it alone")
    print("leave - Leave the battlefield")

    choice = input("Enter your choice: ").lower()
    if choice == "ally":
        print("You ally with Lancelot and his army and prepare for battle.")
    elif choice == "go alone":
        print("You go it alone and prepare for battle.")
    elif choice == "leave":
        print("You leave the battlefield and head towards the dungeon.")
        break

print("\nDungeon: Aiden must navigate a dungeon to reach Saron's lair.")
while True:
    print("\nWhat would you like to do in the dungeon?")
    print("unlock - Unlock a door")
    print("avoid - Avoid a trap")
    print("take - Take some treasure")
    print("leave - Leave the dungeon")

    choice = input("Enter your choice: ").lower()
    if choice == "unlock":
        print("You unlock a door and move closer to Saron's lair.")
    elif choice == "avoid":
        print("You successfully avoid a trap and continue your journey.")
    elif choice == "take":
        print("You take some treasure and add it to your collection.")
    elif choice == "leave":
        print("You leave the dungeon and head towards Saron's lair.")
        break

print("\nLairs: Aiden must defeat Saron and save Isabella.")
while True:
    print("\nWhat would you like to do in Saron's lair?")
    print("cast - Cast a spell")
    print("avoid - Avoid a spell")
    print("free - Free Isabella")
    print("leave - Leave Saron's lair")

    choice = input("Enter your choice: ").lower()
    if choice == "cast":
        print("You cast a spell and defeat Saron.")
    elif choice == "avoid":
        print("You successfully avoid Saron's spell and continue the battle.")
    elif choice == "free":
        print("You free Isabella and save her from Saron's grasp.")
    elif choice == "leave":
        print("You leave Saron's lair and return home as a hero.")
        break

print("\nCongratulations! You have completed Aiden's Adventure.")
