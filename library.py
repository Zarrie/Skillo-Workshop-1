class Library:
    def __init__(self, library_id, address):
        self.library_id = library_id
        self.address = address
        self.__books_list = []
        self.__rented_books = []
        self.__readers = set()

    def add_book(self, book):
        self.__books_list.append(book)

    def remove_book(self, book, remove_all=False):
        if remove_all:
            # Option 1
            # new_books_list = []
            # for current_book in self.__books_list:
            #     if current_book != book:
            #         new_books_list.append(current_book)
            #
            # self.__books_list = new_books_list

            # Option 2
            book_occurrences = self.__books_list.count(book)
            for i in range(book_occurrences):
                self.__books_list.remove(book)

            # Explanation of Option 2
            # problem - remove the number 3 ( all occurs )
            # [1, 2, 3, 3, 4, 5, 3].remove(3)
            # [1, 2, 3, 4, 5, 3].remove(3)
            # [1, 2, 4, 5, 3].remove(3)
            # [1, 2, 4, 5]
        else:
            self.__books_list.remove(book)

    def rent_book(self, book, reader):
        if reader not in self.__readers:
            return "You are not a member of our Library and you can't rent our books."

        if len(reader.get_rented_books()) >= 2:
            return "You already have rented 2 books and cannot rent more."

        is_available = False

        for current_book in self.__books_list:
            if current_book == book:
                is_available = True
                break

        if is_available:
            self.remove_book(book)
            self.__rented_books.append(book)
            reader.rent_book(book)
        else:
            return "Book not available"

    def return_book(self, book, reader):
        self.__rented_books.remove(book)
        self.__books_list.append(book)

        reader.return_book(book)

    def get_available_books(self):
        result = []
        for book in self.__books_list:
            result.append(str(book))
        return result

    def get_rented_books(self):
        result = []
        for book in self.__rented_books:
            result.append(str(book))
        return result

    def add_reader(self, reader):
        self.__readers.add(reader)

    def remove_reader(self, reader):
        self.__readers.remove(reader)

    def __str__(self):
        return self.address
