from db_connect import connect_db

# Add new student
def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    phone = input("Enter phone: ")

    query = "INSERT INTO students(student_id, name, branch, phone) VALUES(%s,%s,%s,%s)"
    cursor.execute(query, (student_id, name, branch, phone))

    conn.commit()
    conn.close()

    print("✅ Student added successfully")


# View all students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM students"
    cursor.execute(query)

    students = cursor.fetchall()

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]}, Branch: {s[2]}, Phone: {s[3]}")

    conn.close()
