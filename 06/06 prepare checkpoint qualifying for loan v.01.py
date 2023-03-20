def loan_decision():
    loan_size = int(input("How large is the loan? (1-10) "))
    credit_history = int(input("How good is your credit history? (1-10) "))
    income = int(input("How high is your income? (1-10) "))
    down_payment = int(input("How large is your down payment? (1-10) "))
    decision = False
    if loan_size >= 5:
        if credit_history >= 7 and income >= 7:
            decision = True
        elif credit_history >= 7 or income >= 7:
            if down_payment >= 5:
                decision = True
    else:
        if credit_history < 4:
            decision = False
        elif income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >= 4:
            decision = True
    return decision

result = loan_decision()
if result:
    print("Yes, you can get the loan.")
else:
    print("No, you cannot get the loan.")