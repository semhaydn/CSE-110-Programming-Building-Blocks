bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3

if extra_cheese == "Y":
    print(f"your final bill is {bill + 1}")
else:
    print(f"your final bill is {bill}")