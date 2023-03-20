# Input the grade percentage
grade = int(input("Enter your grade percentage: "))

# Initialize the letter grade variable
letter = ""

# Determine the letter grade based on the grade percentage
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Print the letter grade
print(f"Your letter grade is: {letter}")

# Check if the student passed the course
if letter != "F":
    print("Congratulations! You passed the class.")
else:
    print("Better luck next time. Keep working hard.")