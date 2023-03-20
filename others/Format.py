first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
email = input("Please enter your email address: ")
phone = input("Please enter your phone number: ")
job_title = input("Please enter your job title: ")
id_num = input("Please enter your ID number: ")

# Convert last name to all caps
last_name = last_name.upper()

# Capitalize first letter of job title
job_title = job_title.title()

# Convert email to lowercase
email = email.lower()

# Define the format string
format_string = """
----------------------------------------
{}, {}
{}
ID: {}

{}
{}
----------------------------------------
"""
# Pass the data as arguments to the format method

print(format_string.format(last_name, first_name, job_title, id_num, email, phone))