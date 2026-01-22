# User Stories
## Library Management System

This document captures the Agile user stories for the Library Management System project.
Each user story follows the standard format:
As a [user role], I want [feature], so that [benefit].

---

### US-01: User Registration
As a library user, I want to register an account, so that I can access library services.

Priority: High

Acceptance Criteria:
- User can register using valid details
- Duplicate registrations are not allowed
- System shows a successful registration message

---

### US-02: User Login
As a registered user, I want to log in to the system, so that I can manage my library activities.

Priority: High

Acceptance Criteria:
- User can log in with valid credentials
- Error message is shown for invalid login
- User session is created after login

---

### US-03: Search Books
As a user, I want to search for books by title, author, or category, so that I can find books easily.

Priority: High

Acceptance Criteria:
- Search returns relevant books
- Multiple search filters are supported
- Message is shown if no books are found

---

### US-04: Issue Book
As a user, I want to issue a book, so that I can borrow it from the library.

Priority: Medium

Acceptance Criteria:
- Book availability is checked before issuing
- Issue date is recorded
- User cannot issue more books than the allowed limit

---

### US-05: Return Book
As a user, I want to return a borrowed book, so that the system updates book availability.

Priority: Medium

Acceptance Criteria:
- Return date is recorded
- Fine is calculated if the book is overdue
- Book becomes available after return

---

### US-06: Admin Add Books
As an admin, I want to add new books to the library, so that users can borrow them.

Priority: High

Acceptance Criteria:
- Admin can add book details
- Duplicate books are handled properly
- Added books appear in search results

---

### US-07: Admin Remove Books
As an admin, I want to remove outdated or damaged books, so that the catalog remains accurate.

Priority: Low

Acceptance Criteria:
- Only admin can remove books
- Removed books are not visible to users
- Removal action is logged

