# 09 Prove: Assignment Milestone 
# Semih Aydin 

items = []

prices = []

new_item = None

action = None

# greeting the user and guiding it
print('Welcome to the Shopping Cart Program!')
print()

# entering to a loop
while action !=  '5':
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = (input(('Please enter an action:  ')))

    # first action
    if action == '1':
        while new_item != 'quit':
            new_item = (input('What item would you like to add? (write quit when you finish) ')) 
            if new_item != 'quit':
                items.append(new_item)
                price = input((f'What is the price of {new_item} ? '))
                prices.append(float(price))
                print(f'{new_item} has been added to the cart.')
                print()
        print()

    # second action 
    elif action == '2':
        print('The contents of the shopping cart are:')
        # for new_item , price in zip(items, prices):
        #     print(f'{new_item} - {price}')
        # print()
        for i in range(len(items)):
            new_item = items[i]
            price = prices[i]
            print(f'{i+1} {new_item} - ${price:.2f}')
        print()

    #third action
    elif action == '3':
        index = (int(input('Which item would you like to remove? '))) - 1
        if index >= 0 and index < len(items): #check if index is valid
            removed_item = items.pop(index)
            prices.pop(index)
            print(f'{removed_item} removed ')
        else:
            print('Invalid number ')
        print()

    elif action == '4':
        total = sum(prices)
        avarage_item = sum(prices) / len(prices)

        print(f'The total price of the items in the shopping cart is {total}')
        print(f'The avarage item costed {avarage_item} ')
        print()
        

else:
    print('Thank you. Goodbye. ')



