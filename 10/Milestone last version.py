# initialize empty lists for items and prices
items = []
prices = []

# initialize variables for user input
new_item = None
action = None

# greet the user and provide program options
print('Welcome to the Shopping Cart Program!\n')
while action != '5':
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = input('\nPlease enter an action: ')

    # action 1: add item to cart
    if action == '1':
        while new_item != 'quit':
            # prompt user for new item name and price
            new_item = input('\nWhat item would you like to add? (write quit when you finish) ')
            if new_item != 'quit':
                price = float(input(f'What is the price of {new_item}? '))
                # add item name and price to respective lists
                items.append(new_item)
                prices.append(price)
                print(f'{new_item} has been added to the cart.\n')
        new_item = None  # reset new_item variable for next loop iteration

    # action 2: view cart
    elif action == '2':
        print('\nThe contents of the shopping cart are:')
        for i in range(len(items)):
            # display item number, name, and price
            print(f'{i+1}. {items[i]} - ${prices[i]:.2f}')
        print()

    # action 3: remove item from cart
    elif action == '3':
        index = int(input('\nWhich item would you like to remove? Enter the item number: ')) - 1
        # check if index is valid
        if index >= 0 and index < len(items):
            removed_item = items.pop(index)  # remove item from items list
            removed_price = prices.pop(index)  # remove corresponding price from prices list
            print(f'{removed_item} has been removed from the cart.\n')
        else:
            print('Invalid item number.\n')

    # action 4: compute total price and average price per item
    elif action == '4':
        total_price = sum(prices)
        avg_price = total_price / len(prices)
        print(f'\nThe total price of the items in the shopping cart is ${total_price:.2f}')
        print(f'The average price per item is ${avg_price:.2f}\n')

    # invalid input: prompt user to enter valid input
    elif action != '5':
        print('Invalid action. Please enter a number from 1 to 5.\n')

# exit program
print('Thank you for using the Shopping Cart Program. Goodbye!')

