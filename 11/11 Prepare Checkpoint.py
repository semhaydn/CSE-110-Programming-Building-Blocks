# 11 Prepare: Checkpoint

with open('books.txt') as books_file:
    for line in books_file:
        line = line.strip()
        print(line)
