CREATE DATABASE library_management_system;
USE library_management_system;
CREATE TABLE books(
book_id INT PRIMARY KEY auto_increment,
title varchar(100),
author varchar(100),
category varchar(50),
quantity int );
create table students(
student_id int primary key,
name varchar(50),
branch varchar(50),
phone varchar(10)
);
create table issued_books(
issue_id int auto_increment primary key,
book_id int,
student_id int,
issue_date date,
return_date date,
status varchar(20),
foreign key(book_id) references books(book_id),
foreign key(student_id) references students(student_id) );
create table admin(
admin_id int auto_increment primary key,
username varchar(50),
password varchar(50) );

INSERT INTO books (title, author, category, quantity) VALUES
('Introduction to Algorithms','Thomas H. Cormen','Computer Science',5),
('Clean Code','Robert C. Martin','Programming',4),
('Database System Concepts','Abraham Silberschatz','Database',6),
('Artificial Intelligence Basics','Tom Taulli','AI',3),
('Operating System Concepts','Abraham Silberschatz','System',7),
('Python Crash Course','Eric Matthes','Programming',8),
('Computer Networks','Andrew S. Tanenbaum','Networking',5),
('Deep Learning','Ian Goodfellow','AI',2),
('The Pragmatic Programmer','Andrew Hunt','Programming',6),
('Discrete Mathematics','Kenneth Rosen','Mathematics',9),
('Digital Logic Design','M. Morris Mano','Electronics',5),
('Data Structures in Python','Michael Goodrich','Programming',7),
('Machine Learning Guide','Andriy Burkov','AI',4),
('Unix Concepts','Sumitabha Das','System',3),
('C Programming Language','Dennis Ritchie','Programming',10),
('Java Complete Reference','Herbert Schildt','Programming',8),
('Software Engineering','Ian Sommerville','SE',6),
('Cloud Computing Basics','Rajkumar Buyya','Cloud',4),
('Cyber Security Essentials','Charles Brooks','Security',5),
('Big Data Analytics','Viktor Mayer','Data Science',3),
('HTML and CSS Design','Jon Duckett','Web',7),
('JavaScript Guide','David Flanagan','Web',6),
('React Explained','Zac Gordon','Web',4),
('Node.js in Action','Mike Cantelon','Backend',5),
('DevOps Handbook','Gene Kim','DevOps',2);

INSERT INTO students (student_id, name, branch, phone) VALUES
(101,'Aman Verma','CSE','9876543210'),
(102,'Rahul Sharma','ISE','9123456780'),
(103,'Sneha Reddy','ECE','9988776655'),
(104,'Priya Nair','CSE','9090909090'),
(105,'Arjun Singh','ME','9012345678'),
(106,'Kiran Kumar','CSE','8899776655'),
(107,'Neha Jain','ISE','8877665544'),
(108,'Rohit Patil','ECE','7766554433'),
(109,'Divya Shetty','CSE','9988001122'),
(110,'Ankit Das','EEE','9900112233'),
(111,'Vikas Yadav','ME','9011223344'),
(112,'Shreya Gupta','CSE','9099887766'),
(113,'Harsha Rao','ISE','9870012345'),
(114,'Megha Pillai','ECE','9123409876'),
(115,'Faizan Khan','CSE','9345678123'),
(116,'Varun N','EEE','9987123456'),
(117,'Tanvi Kulkarni','ISE','9090901234'),
(118,'Abhishek Roy','CSE','9000011122'),
(119,'Pooja Sharma','ECE','9556677889'),
(120,'Nikhil Jain','CSE','9887766554');

INSERT INTO issued_books (book_id, student_id, issue_date, return_date, status) VALUES
(1,101,'2026-01-05','2026-01-15','Returned'),
(2,102,'2026-01-10',NULL,'Issued'),
(3,103,'2026-01-12',NULL,'Issued'),
(4,104,'2026-01-15','2026-01-25','Returned'),
(5,105,'2026-01-18',NULL,'Issued'),
(6,106,'2026-01-20','2026-01-30','Returned'),
(7,107,'2026-01-22',NULL,'Issued'),
(8,108,'2026-01-25',NULL,'Issued'),
(9,109,'2026-01-27','2026-02-02','Returned'),
(10,110,'2026-01-28',NULL,'Issued'),
(11,111,'2026-01-30','2026-02-05','Returned'),
(12,112,'2026-02-01',NULL,'Issued'),
(13,113,'2026-02-02',NULL,'Issued'),
(14,114,'2026-02-03','2026-02-09','Returned'),
(15,115,'2026-02-04',NULL,'Issued'),
(16,116,'2026-02-05',NULL,'Issued'),
(17,117,'2026-02-06','2026-02-12','Returned'),
(18,118,'2026-02-07',NULL,'Issued'),
(19,119,'2026-02-08',NULL,'Issued'),
(20,120,'2026-02-09','2026-02-13','Returned'),
(21,101,'2026-02-10',NULL,'Issued'),
(22,102,'2026-02-11',NULL,'Issued'),
(23,103,'2026-02-12',NULL,'Issued'),
(24,104,'2026-02-12',NULL,'Issued'),
(25,105,'2026-02-13',NULL,'Issued');

INSERT INTO admin (username, password) VALUES
('admin','admin123'),
('librarian','lib123'),
('dsu_admin','dsu2026'),
('testuser','test123');


alter table issued_books 
add fine int;
