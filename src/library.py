class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    raise ValueError("Book already borrowed")
                book.is_borrowed = True
                return
        raise ValueError("Book not found")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    raise ValueError("Book is not borrowed")
                book.is_borrowed = False
                return
        raise ValueError("Book not found")

    def generate_report(self) -> str:
        report = ["ID | Title | Author | Status"]

        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            report.append(
                f"{book.book_id} | {book.title} | {book.author} | {status}"
            )

        return "\n".join(report)

