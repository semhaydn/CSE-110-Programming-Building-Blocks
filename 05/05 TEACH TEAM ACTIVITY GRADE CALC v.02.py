grade = int(input("Enter your percentage grade: "))

letter = ""
sign = ""
if grade >= 90:
    letter = "A"
    if grade % 10 >= 7:
        sign = "-"
elif grade >= 80:
    letter = "B"
    if grade % 10 >= 7:
        sign = "+"
    elif grade % 10 < 3:
        sign = "-"
elif grade >= 70:
    letter = "C"
    if grade % 10 >= 7:
        sign = "+"
    elif grade % 10 < 3:
        sign = "-"
elif grade >= 60:
    letter = "D"
    if grade % 10 >= 7:
        sign = "+"
    elif grade % 10 < 3:
        sign = "-"
else:
    letter = "F"

if letter == "A" and sign == "+":
    sign = ""
if letter == "F":
    sign = ""

print("Your letter grade is:", letter + sign)

if grade >= 70:
    print("Congratulations, you passed the course!")
else:
    print("Better luck next time. Keep up the hard work.")