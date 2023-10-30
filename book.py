class Book:
    def __init__(self, title, author, genre, release_date, book_id):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.release_date = release_date

    def __eq__(self, other):
        if self.title == other.title and \
                self.author == other.author and \
                self.release_date == other.release_date:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title}, {self.author}, {self.release_date}"
