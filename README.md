# 📚 backend-library-system
A backend-based Library Management System built using Python and MySQL to manage book issuing, returning, and inventory tracking with automatic fine calculation.

🚀 Features

Add and manage books

Register students

Issue books with due date tracking

Return books with automatic fine calculation

Inventory quantity updates

Proper edge case handling

🛠️ Tech Stack

Python

MySQL

mysql.connector

SQL functions (DATEDIFF, CURDATE, GREATEST)

📂 Database Tables

books → book_id, title, author, quantity

students → student_id, name, department

issue_books → issue_id, student_id, book_id, issue_date, due_date, return_date, status

🔧 Core Functions
➤ issue_book()
Checks stock availability
Sets issue_date and due_date (7-day rule)
Reduces book quantity

➤ return_book(issue_id)
Validates issue record
Calculates fine using:
GREATEST(DATEDIFF(CURDATE(), due_date), 0) * 5
Updates return_date and status
Increases book quantity
Prevents duplicate returns

⚠ Edge Case Handling

Invalid issue ID

Already returned book

No stock available

Early return (no negative fine)

📈 Future Improvements

Fine history tracking

Grace period support

Admin authentication

Flask API / Full-stack version

🎯 Purpose

This project demonstrates backend development concepts such as:

SQL date handling

Transaction management

CRUD operations

Business logic implementation
