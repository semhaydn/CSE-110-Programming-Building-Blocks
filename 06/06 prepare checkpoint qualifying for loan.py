# 06 Prepare: Checkpoint Qualifying for a Loan

# Import the time
from datetime import datetime

# A warm welcome to customer
greeting = 'Thank you for choosing'

bank_name = 'Golden Horizon Bank'
address_line1 = '3477 Broadway'
address_line2 = 'New York, NY 10031'

# We will use "*" To seperate the parts of the receipt
print('*' * 70) 

#Header
print(f'{"LOAN QUALIFIER":^70}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)

#Blank Space
print('\n')

#Displaying the greeting and information about the store
print(f'{greeting:^70}')
print(f'{bank_name:^70}')
print(f'{address_line1:^70}')
print(f'{address_line2:^70}')

#Blank Space
print('\n')

# Prompting the date
current_date = datetime.now().date()
print(f'Date: {current_date.strftime("%Y-%m-%d")}')

# Promting the time
current_time = datetime.now().time()
print(f'Time: {current_time.strftime("%H:%M:%S")}')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)


# Questioning the customer
# First question

print('Please answer the questions below, with a rating from 1-10. ')

loan = int(input('How large is the loan? '))

credit = int(input('How good is your credit history? '))

income = int(input('How high is your income? '))

down_payment = int(input('How large is your down payment? '))

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True 

    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False

else:
    if credit <4:
        decision = False
    elif income >= 7 or down_payment >= 7:
        decision = True
    elif income >= 4 and down_payment >= 4:
        decision = True
    else:
        decision = False

# Blank Space
print('\n')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)


# Displaying the decision

if decision:
    print('You are eligible to receive a credit! ')

else:
    print('Unfortunately you are not eligible for a credit. ')

# Blank Space
print('\n')

# We will use "*" To seperate the parts of the receipt
print('*' * 70)