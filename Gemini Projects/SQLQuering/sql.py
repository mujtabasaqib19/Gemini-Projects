import sqlite3

#connect to sqlite
connect = sqlite3.connect("employees.db")

cursor = connect.cursor()

table = """
CREATE TABLE IF NOT EXISTS EMPLOYEES (
    NAME VARCHAR(25),
    DEPARTMENT VARCHAR(25),
    SALARY INT,
    JOB_TITLE VARCHAR(25)
);
"""

cursor.execute(table)

#insert records
cursor.executemany("""
INSERT INTO EMPLOYEES (NAME, DEPARTMENT, SALARY, JOB_TITLE) 
VALUES (?, ?, ?, ?)
""", [
    ('Alice Johnson', 'Computer Science', 65000, 'Software Engineer'),
    ('Bob Smith', 'Electrical Engineering', 58000, 'Hardware Engineer'),
    ('Charlie Brown', 'Mechanical Engineering', 60000, 'Design Engineer'),
    ('Diana Prince', 'Business Administration', 72000, 'Project Manager'),
    ('Evan Taylor', 'Computer Science', 70000, 'Data Scientist')
])

#display records
data = cursor.execute('''SELECT * FROM EMPLOYEES''')

for row in data:
    print(row)
    
#close the connection
connect.commit()
connect.close()

