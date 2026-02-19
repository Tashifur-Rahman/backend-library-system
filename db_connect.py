import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tashif0810",
        database="library_management_system"
    )
