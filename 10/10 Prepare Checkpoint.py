# Week 10 prepare : check point 
# Semih Aydin 

# ask for shopping list items

Shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish):")

item = None

while item != 'quit':
    item = (input('Item: '))
    if item != 'quit':
        Shopping_list.append(item)

# print original shopping list 

print("\nThe shopping list is:")
for item in Shopping_list:
        print(item)

# Print shopping list with indexes

print("\nThe shopping list with indexes is:")
for index in range(len(Shopping_list)):
     print(f'{index}. {Shopping_list[index]}')

# Ask for index and new item
index_new = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

Shopping_list[index_new] = new_item

# Print updated shopping list
print("\nThe shopping list with indexes is:")
for index in range(len(Shopping_list)):
    print(f"{index}. {Shopping_list[index]}")