# https://byui-cse.github.io/cse110-course/lesson02/teach.html
# 02 Teach: Programming Activity

print("Please enter the following information:\n")

first_name = input("First name: ")
last_name = input("Last name: ").upper()
email = input("Email address: ").lower()
phone_number = input("Phone number: ")
job_title = input("Job title: ").title()
id_number = input("ID Number: ")
hair = input("Hair color: ")
eyes = input("Eye color: ")
month = input("Month started: ")
training = input("Completed advanced training? (yes/no): ")

print("\nID Card:")
print("-" * 40)
print(f"{last_name}, {first_name}")
print(job_title)
print(f"ID: {id_number}\n")
print(email)
print(phone_number)
print(f"\nHair: {hair:<15} Eyes: {eyes}")
print(f"Month: {month:<14} Training: {training}")
print("-" * 40)
