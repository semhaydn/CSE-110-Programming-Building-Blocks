def calculate_tax(province):
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        return 0.05
    elif province == 'Ontario':
        return 0.13
    else:
        return 0.12

def calculate_total(price, tax_rate):
    sales_tax = price * tax_rate 
    total = price + sales_tax
    return total

def calculate_tip(total, tip_amount):
    return total + tip_amount

print('Welcome to the Sales Tax Calculator!')
country = input('Where are you from? ')

if country.lower() == 'canada':
    print('\nCanadian provinces with their corresponding tax rate:')
    print('Alberta, Nunavut, Yukon: 5%')
    print('Ontario: 13%')
    print('Other provinces: 12%')
    province = input('Which province are you from? ')
    tax_rate = calculate_tax(province)
else:
    tax_rate = 0.00

price = float(input('\nHow much did you pay? $'))
total = calculate_total(price, tax_rate)

print(f'\nSubtotal: ${price:.2f}')
print(f'Sales Tax ({tax_rate*100}%): ${price * tax_rate:.2f}')
print(f'Total: ${total:.2f}')

tip = float(input('\nWould you like to leave a tip? If so, what percentage? '))
tip_amount = total * tip / 100
total_with_tip = calculate_tip(total, tip_amount)

print(f'Tip Amount ({tip}%): ${tip_amount:.2f}')
print(f'Grand Total: ${total_with_tip:.2f}')