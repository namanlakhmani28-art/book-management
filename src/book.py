class Book:
    def borrow(self):
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def __init__(self, book_id, title, author="Unknown"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

