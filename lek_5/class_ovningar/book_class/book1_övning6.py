from book import Book

book_list = []

book_list.append(Book ("1984", "George Orwell"))
book_list.append(Book("Främlingen", "Albert Camus"))
book_list.append(Book("Pälsen", "Hjalmar Söderberg"))

for book in book_list:
    print(book.summary())