from library import Library

def test_report_contains_header():
    library = Library()
    report = library.generate_report()

    assert "ID | Title | Author | Status" in report

