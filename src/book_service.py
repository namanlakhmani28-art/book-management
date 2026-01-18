class BookAlreadyExistsError(Exception):
    pass


class BookService:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise BookAlreadyExistsError("Book ID already exists")

        self.books[book_id] = {
            "id": book_id,
            "title": title,
            "author": author
        }

