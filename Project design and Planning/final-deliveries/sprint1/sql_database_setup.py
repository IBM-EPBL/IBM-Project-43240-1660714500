import sqlite3

conn = sqlite3.connect('costomerdatabase.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT,phone TEXT,email TEXT, password text,addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")
conn.close()