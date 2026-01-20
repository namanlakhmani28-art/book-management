from library import Library
from book import Book

def test_report_contains_book_entry():
    library = Library()
    book = Book(1, "Clean Code", "Robert C. Martin")
    library.add_book(book)

    report = library.generate_report()

    assert "Clean Code" in report
    assert "Available" in report

