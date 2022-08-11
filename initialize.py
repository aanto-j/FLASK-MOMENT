import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('drop table student')

cursor.execute('''create table student(
    name varchar(20),
    age number(3),
    rollno number(12) primary key
)''')

