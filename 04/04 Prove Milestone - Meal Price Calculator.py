# 03 Prove: Milestone - Meal Price Calculator

# Import the time
from datetime import datetime

# A warm welcome to customer
greeting = 'Thank you for choosing'

# information about the company
store_name = "Mama John's"
address_line1 = '3477 Broadway'
address_line2 = 'New York, NY 10031'

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

# Header
print(f'{"RECEIPT":^70}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

# Blank Space
print('\n')

# Displaying the greeting and information about the store
print(f'{greeting:^70}')
print(f'{store_name:^70}')
print(f'{address_line1:^70}')
print(f'{address_line2:^70}')

# Blank Space
print('\n')

# Prompting the date
current_date = datetime.now().date()
print(f'Date: {current_date.strftime("%Y-%m-%d")}')

# Promting the time
current_time = datetime.now().time()
print(f'Time: {current_time.strftime("%H:%M:%S")}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

# Child Meal
child_meal_price = float(input("What is the price of a child's meal? :"))

# Adult meal
adult_meal_price = float(input("What is the price of an adult's meal? :"))

# Number of children
number_of_children = int(input('How many children are there? :'))

# Number of adults
number_of_adults = int(input('How many adults are there? :'))

# Sales tax rate
tax_rate = float(input('What is the sales tax rate? :'))

# Calculating Childeren total price
childeren_total = (child_meal_price * number_of_children)

# Calculating Adult total price
adult_total = (adult_meal_price * number_of_adults)

# Calculating sub total
sub_total = (childeren_total + adult_total)

# leaving empty spaces
print('')

# Displaying the sub total
print(f'Subtotal: ${sub_total:.2f}')

# Calculating the sales tax
sales_tax = sub_total*tax_rate/100

# Displaying the sales tax
print(f'Sales Tax: ${sales_tax:.2f}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

# Calculating the total
total = sub_total+sales_tax

# Adding point system
points = int(total)
print(f'You earned {points} points! You can use your points on our webpage!')

# leaving empty spaces
print('')

# Displaying the total
print(f'Total: ${total:.2f}')

# leaving empty spaces
print('')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

# Adding tip system
tip_percentage = float(input('Enter tip percentage (5, 10, or 15): '))
tip_amount = total * (tip_percentage / 100)
print(f'Tip amount: ${tip_amount:.2f}')

# leaving empty spaces
print('')

# Calculating the total with tip
total_with_tip = total + tip_amount

# Displaying the total with tip
print(f'Total with tip amount: ${total_with_tip:.2f}')

# Payment Amount
payment_amount = float(input('What is the payment amount? '))
while payment_amount < total_with_tip:
    print('Payment amount must be greater than or equal to total with tip.')
    payment_amount = float(input('What is the payment amount? '))

# Calculating the change
change = payment_amount-total_with_tip

# Displaying the change
print(f'Change: ${change:.2f}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)