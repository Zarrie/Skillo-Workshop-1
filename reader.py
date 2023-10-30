class Reader:
    def __init__(self, reader_id, name, pin):
        self.__reader_id = reader_id
        self.name = name
        self.pin = pin
        self.__rented_books = []

    def rent_book(self, book):
        self.__rented_books.append(book)

    def return_book(self, book):
        self.__rented_books.remove(book)

    def get_rented_books(self):
        result = []
        for book in self.__rented_books:
            result.append(str(book))
        return result
