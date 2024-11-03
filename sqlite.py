import sqlite3

## connect to sqlite database
connection = sqlite3.connect("student.db")

## create a cursor onject to insert record, create table
cursor = connection.cursor()

## create table
table_info = """
    CREATE TABLE STUDENT(NAME VARCHAR(20), CLASS VARCHAR(20), SECTION VARCHAR(25), MARKS INT)
"""
cursor.execute(table_info)

## insert record
cursor.execute("INSERT INTO STUDENT VALUES('John', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Onur', 'Deep Learning', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Ilhan', 'Data Science', 'A', 95)")
cursor.execute("INSERT INTO STUDENT VALUES('Asim', 'Machine Learning', 'B', 85)")

## display all the recors
print("All the records in the table")
data = cursor.execute("SELECT * FROM STUDENT")
for record in data:
    print(record)

connection.commit()
connection.close()