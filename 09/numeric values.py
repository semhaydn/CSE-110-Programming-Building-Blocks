friends = ['Batuhan','Emre','Egemen']
tips = [12.25, 13.95 , 8.50]

running_total = 0

for tip_amount in tips:
    running_total += tip_amount


print(f'The total is: {running_total:.2f}')
