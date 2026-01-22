# Requirements Traceability Matrix (RTM)

## Project: Library Management System

This document provides complete **requirements traceability** for the Library Management System.  
It maps requirements to user stories, modules, code components, and test cases to ensure
that every requirement is properly implemented and verified.

---

## 1. Purpose of Traceability

The purpose of this traceability file is to:
- Ensure all functional requirements are implemented
- Maintain alignment between requirements, development, and testing
- Track project completeness and quality
- Support Agile development and future maintenance

---

## 2. Traceability Flow

Requirement → User Story → Module → Code → Test Case → Status

---

## 3. Functional Requirements

| Requirement ID | Description |
|---------------|-------------|
| FR-01 | User authentication (login/logout) |
| FR-02 | Admin can add new books |
| FR-03 | Admin can update book details |
| FR-04 | Admin can delete books |
| FR-05 | User can search books |
| FR-06 | User can issue a book |
| FR-07 | User can return a book |
| FR-08 | System calculates fine for late return |
| FR-09 | User can view issued books |
| FR-10 | Admin can manage users |

---

## 4. User Stories

| User Story ID | User Story |
|--------------|------------|
| US-01 | As a user, I want to log in so that I can access the system |
| US-02 | As an admin, I want to add books so that users can borrow them |
| US-03 | As an admin, I want to update book details |
| US-04 | As an admin, I want to delete books |
| US-05 | As a user, I want to search for books easily |
| US-06 | As a user, I want to issue books |
| US-07 | As a user, I want to return issued books |
| US-08 | As a system, I want to calculate fines automatically |
| US-09 | As a user, I want to view my issued books |
| US-10 | As an admin, I want to manage users |

---

## 5. Requirements Traceability Matrix

| Req ID | User Story ID | Module | Code File | Test Case ID | Status |
|------|--------------|--------|----------|--------------|--------|
| FR-01 | US-01 | Authentication | authController.java | TC-01 | Completed |
| FR-02 | US-02 | Book Management | bookService.java | TC-02 | Completed |
| FR-03 | US-03 | Book Management | bookService.java | TC-03 | Completed |
| FR-04 | US-04 | Book Management | bookService.java | TC-04 | Completed |
| FR-05 | US-05 | Search | searchService.java | TC-05 | Completed |
| FR-06 | US-06 | Issue Book | issueController.java | TC-06 | Completed |
| FR-07 | US-07 | Return Book | returnController.java | TC-07 | Completed |
| FR-08 | US-08 | Fine Calculation | fineService.java | TC-08 | Completed |
| FR-09 | US-09 | User Dashboard | dashboardController.java | TC-09 | Completed |
| FR-10 | US-10 | User Management | userService.java | TC-10 | Completed |

---

## 6. Test Case Summary

| Test Case ID | Description |
|-------------|-------------|
| TC-01 | Verify user login |
| TC-02 | Verify add book functionality |
| TC-03 | Verify update book functionality |
| TC-04 | Verify delete book functionality |
| TC-05 | Verify book search |
| TC-06 | Verify book issue |
| TC-07 | Verify book return |
| TC-08 | Verify fine calculation |
| TC-09 | Verify issued books list |
| TC-10 | Verify user management |

---

## 7. Status Legend

- Completed – Implemented and tested  
- In Progress – Under development  
- Pending – Not started  

---

## 8. Conclusion

This Requirements Traceability Matrix ensures complete coverage of all functional
requirements of the Library Management System and supports quality-driven
Agile development.

