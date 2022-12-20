# import sqlite3



# def create_connection(db_file):
#     '''
#     Create a database connection to a SQLite database
    
#     '''
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print("Sqlite version:", sqlite3.version)
#     except sqlite3.Error as ex:
#         print(ex)
#     finally:
#         if conn:
#             conn.close()

# #create_connection('hr.db')
# conn = sqlite3.connect('hr.db')
# print(conn)
# cursor = conn.execute("""select name from sqlite_schema
#                 where type = 'table';
#             """)

# for row in cursor:
#     print(row)

import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Sqluite version", sqlite3.version)
    except sqlite3.Error as ex:
        print(ex)
    finally:
        if conn:
            conn.close()

create_connection("hr.db")
conn = sqlite3.connect("hr.db")

cursor = conn.execute("""
SELECT employee_id, department_id 
FROM 'employees' 
WHERE salary BETWEEN 3000 AND 6000;""")

for row in cursor:
    print(row)

cursor = conn.execute("""
SELECT employee_id, email
FROM employees
WHERE email LIKE 'P%' OR email LIKE 'A%';
""")

for row in cursor:
    print(row) 