friends = []

new_friend = ""
while new_friend != "end":
    new_friend = input('Type the name of a friend? (Type "end" when you are done) ')
    friends.append(new_friend)

print()
print('Your friends are :')

for friend in friends:
    if friend != 'end':
        print(friend)
    

# clients.append('Emily')

# clients.append('John')

# clients.append('Mary')

