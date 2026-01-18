import pytest
from src.book_service import BookService, BookAlreadyExistsError

def test_add_book_success():
	service = BookService()
	service.add_book("B101", "Clean Code", "Robert C. Martin")
	
	assert "B101" in service.books
	
	
def test_add_duplicate_book():
	service = BookService()
	service.add_book("B101", "Clean Code", "Robert C. Martin")
	
	with pytest.raises(BookAlreadyExistsError):
		service.add_book("B101", "Refactoring", "Martin Fowler")

