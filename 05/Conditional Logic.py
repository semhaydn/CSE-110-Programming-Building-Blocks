# if price >= 1.00:
#     tax = .07
#     # print =(tax)
# else :
#     tax = 0
#     print(tax)

country = input('Where are you from ?')

if country.lower() == 'canada':
    province = input('Which province are you from ?')
    if province.lower() in ('alberta', 'nunavut', 'yukon'):
        tax_rate = 0.05
    elif province.lower() == 'ontario':
        tax_rate = 0.13
    else:
        tax_rate = 0.15
else:
    tax_rate = 0.00

price = float(input('How much did you pay? '))
sales_tax = price * tax_rate 
total = price + sales_tax

print(f'Subtotal: ${price:.2f}')
print(f'Sales Tax ({tax_rate*100}%): ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

tip = float(input('Would you like to leave a tip? If so, what percentage? '))
tip_amount = total * tip / 100
print(f'Tip Amount ({tip}%): ${tip_amount:.2f}')
print(f'Grand Total: ${total + tip_amount:.2f}')




# price=float(input('How much did you pay? '))

# if price >= 1.00:
#     tax_rate = .07
# else:
#     tax_rate = 0
# print(f'Your tax rate is {tax_rate}')



