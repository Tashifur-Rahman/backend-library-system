from book import *
from issue import *
from student import *
while True:
    print("====LIBRARY MANAGEMENT SYSTEM====")
    print("1.Add Book")
    print("2.View Book")
    print("3.Add student")
    print("4.View student")
    print("5.Issue Book")
    print("6.Return Book")
    print("7.View books by category")
    print("8.View books by title")
    print("=================================")
    choice =input("Enter choice: ")
    if choice=="1":
        add_book()
    elif choice=="2":
        view_books()
    elif choice=="3":
        add_student()
    elif choice=="4":
        view_students()
    elif choice=="5":
        issue_book()
    elif choice=="6":
        return_book1()
    elif choice=="7":
        view_books_bycategory()
    elif choice=="8":
        view_books_bytitle()
    else:
        break