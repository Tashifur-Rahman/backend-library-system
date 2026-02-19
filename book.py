from db_connect import connect_db

def add_book():
    conn = connect_db()
    cursor = conn.cursor()

    title = input("Enter title: ")
    author = input("Enter author: ")

    query = "INSERT INTO books(title,author) VALUES(%s,%s)"
    cursor.execute(query,(title,author))

    conn.commit()
    conn.close()

def view_books():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM books"
    cursor.execute(query)

    books = cursor.fetchall()

    print("\n--- Book List ---")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Quantity: {book[4]}")

    conn.close()
def view_books_bycategory():
    conn=connect_db()
    cursor=conn.cursor()
    category=input("Enter the category\n")
    query="SELECT * FROM books WHERE category=%s"
    cursor.execute(query,(category,))
    books=cursor.fetchall()
    if not books:
        print("Can't find books of category:",category)
        return
    else:
        print("\n---Book of category ",(category))
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Quantity: {book[4]}")
    conn.close()
def view_books_bytitle():
    conn=connect_db()
    cursor=conn.cursor()

    title=input("Enter book title\n")
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, (f"%{title}%",))
    books=cursor.fetchall()
    if not books:
        print("Can't find books of title:",title)
        return
    else:
        
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Quantity: {book[4]}")
    conn.close()