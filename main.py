from book import Book
from library import Library
from reader import Reader

book1 = Book(title="Harry Potter 1",
             author="J.K.Rowling",
             genre="Fantasy",
             release_date="01/04/1999",
             book_id=1)

book2 = Book(title="Harry Potter 1",
             author="J.K.Rowling",
             genre="Fantasy",
             release_date="01/04/1999",
             book_id=2)

book3 = Book(title="Harry Potter 2",
             author="J.K.Rowling",
             genre="Fantasy",
             release_date="15/05/2001",
             book_id=3)


print(book1)
print(book2)
print(book1 == book2)
print(book1 == book3)

library1 = Library(library_id=1,
                   address="Sofia, Pozitano 2")

reader1 = Reader(reader_id=1,
                 name="Viktor",
                 pin="9999999999")

library1.add_reader(reader1)

print(library1.get_available_books())

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

print(library1.get_available_books())

library1.rent_book(book1, reader1)
library1.rent_book(book2, reader1)
library1.rent_book(book3, reader1)

print(library1.get_available_books())
print(library1.get_rented_books())

print(library1)

print(reader1.get_rented_books())

print(library1.get_available_books())
print(reader1.get_rented_books())

library1.return_book(book=book2,
                     reader=reader1)

print(library1.get_available_books())
print(reader1.get_rented_books())
