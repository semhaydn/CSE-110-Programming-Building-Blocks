# 10 Teach: Team Activity
# Multiple Lists
# Semih Aydin 

bank_accounts = []

balances = []

new_account = None

new_balance = None 

print('Enter the names and balances of bank accounts (type: quit when done) ')

# Create a loop and getting the info from the user

while new_account != 'quit':
    new_account = input('What is the name of this account? ') 



# Adding the items to the lists
    if new_account != 'quit':
        new_balance = input('What is the balance? ')
        bank_accounts.append(new_account)
        if new_balance.isdigit:
            balances.append(float(new_balance))


# Displaying the items to the user
print('\nAccount information:')
for new_account , new_balance in zip(bank_accounts, balances):
    print(f'{new_account} - {new_balance}')


# Calculating the sum and the avarage of the balances
sum_of_balances = sum(balances)
avarage_of_balances = sum(balances) / len(balances)


# Displaying the sum and the avarage of the balances to the user
print()
print(f'Total: {sum_of_balances:.2f}')
print(f'Avarage {avarage_of_balances:.2f}')





    
