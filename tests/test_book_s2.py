import sys
import os
import pytest

# Add src folder to path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from book import Book


def test_borrow_available_book():
    book = Book("1", "Clean Code")
    book.borrow()
    assert book.is_borrowed is True


def test_borrow_unavailable_book_raises_error():
    book = Book("1", "Clean Code")
    book.borrow()
    with pytest.raises(ValueError):
        book.borrow()


def test_return_book_updates_status():
    book = Book("1", "Clean Code")
    book.borrow()
    book.return_book()
    assert book.is_borrowed is False

