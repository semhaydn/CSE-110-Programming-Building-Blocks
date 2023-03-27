# https://byui-cse.github.io/cse110-course/lesson12/teach.html 

# 12 Teach: Team Activity
# Finding Items in a File

# Semih Aydin

# giving a starting value for both 

largest_chapter = -1
largest_book = ""

chosen_scripture = input('Which volume of scripture you would like to learn ? ')

# Open and read through the file
with open('books_and_chapters.txt') as file:
    # iterating 
    for line in file:
        # getting rid of the white spaces and splitting the collumns   
        clean_line = line.strip()
        parts = clean_line.split(':')

        # naming the parts of the lines so that we can add each part to related list
        scripture = parts[2]
        book = parts[0]
        chapter = int(parts[1])

        # Check if it is same as the user chosen
        if scripture.lower() == chosen_scripture.lower():

            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")

        # finding the largest chapter
            if chapter > largest_chapter:
            # it is the largest
                largest_chapter = chapter
            # name of the book
                largest_book = book

print()


# Displaying to user
print(f'The book that has the largest number of chapters is {largest_book} with {largest_chapter} chapters.')

print()
