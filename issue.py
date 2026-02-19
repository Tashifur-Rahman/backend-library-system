from db_connect import connect_db
from datetime import *
# Issue a book
def issue_book():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID: ")

    # 1️⃣ Check book quantity
    cursor.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
    result = cursor.fetchone()

    if result is None:
        print("❌ Book not found")
        conn.close()
        return

    quantity = result[0]

    if quantity <= 0:
        print("❌ Book not available")
        conn.close()
        return

    # 2️⃣ Insert into issued_books
    issue_query = """
        INSERT INTO issued_books(book_id, student_id, issue_date)
        VALUES(%s,%s,CURDATE())
    """
    cursor.execute(issue_query, (book_id, student_id))

    # 3️⃣ Reduce quantity
    update_query = "UPDATE books SET quantity = quantity - 1 WHERE book_id=%s"
    cursor.execute(update_query, (book_id,))

    conn.commit()
    conn.close()

    print("✅ Book issued successfully")


# Return a book

def return_book():
    conn = connect_db()
    cursor = conn.cursor()

    issue_id = input("Enter issue ID: ")

    # 1️⃣ Get book_id from issued_books
    cursor.execute("SELECT book_id FROM issued_books WHERE issue_id=%s", (issue_id,))
    result = cursor.fetchone()

    if result is None:
        print("❌ Issue record not found")
        conn.close()
        return

    book_id = result[0]

    # 2️⃣ Update return date
    return_query = """
        UPDATE issued_books
        SET return_date = CURDATE()
        WHERE issue_id=%s
    """
    cursor.execute(return_query, (issue_id,))

    # 3️⃣ Increase quantity
    update_book = "UPDATE books SET quantity = quantity + 1 WHERE book_id=%s"
    cursor.execute(update_book, (book_id,))

    conn.commit()
    conn.close() 

    print("✅ Book returned successfully")

def return_book1():
    conn=connect_db()
    cursor=conn.cursor()

    issue_id=input("Enter issue id\n")
    cursor.execute("SELECT book_id,issue_date,status FROM issued_books WHERE issue_id=%s",(issue_id,))
    result=cursor.fetchone()
    
    if result is None:
        print("no issue record found\n")
        conn.close()
        return 
    book_id=result[0]
    issue_date=result[1]
    status=result[2]
    if status=="Returned":
        print("Book has already been returned\n")
        conn.close()
        return
    query="UPDATE issued_books SET return_date=CURDATE() WHERE issue_id=%s"
    cursor.execute(query,(issue_id,))
    today = date.today()
    no_of_days = (today - issue_date).days
    fine=0
    if no_of_days>7:
        fine=(no_of_days-7)*5
    cursor.execute(
    "UPDATE issued_books SET return_date=%s, fine=%s, status=%s WHERE issue_id=%s",
    (today, fine, "Returned", issue_id)
)


    update_book = "UPDATE books SET quantity = quantity + 1 WHERE book_id=%s"
    cursor.execute(update_book, (book_id,))

    conn.commit()
    conn.close()
    print("✅ Book returned successfully")    

