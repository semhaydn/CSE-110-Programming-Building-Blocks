# 09 Teach: Team Activity Lists of Numbers

numbers = []

new_number = None
while new_number != "0":
    new_number = input('Enter a list of numbers, type 0 when finished. ')
    if new_number.isdigit():
        if new_number != "0":
            numbers.append(int(new_number))
    
sum_of_numbers = sum(numbers)
avarage_of_list = sum(numbers) / len(numbers)
largest_number = max(numbers)

print()
print(sum_of_numbers)
print(avarage_of_list)
print(largest_number)

