import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="123abiMahesh"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
connection.database = "employee_db"

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
          id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            position VARCHAR(255),
            salary DECIMAL(10, 2),
            hire_date DATE
    )
    """)
create_table()
def add():
    name = "John Doe"
    position = "Software Engineer"
    salary = 75000.00
    hire_date = "2024-07-01"

    insert_query = "INSERT INTO employees (name, position, salary, hire_date) VALUES('{}','{}','{}','{}')".format(name, position, salary, hire_date)
    cursor.execute(insert_query)
    connection.commit()

    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        print(row)


add()