import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="123abiMahesh",
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS engineer_db")
connection.database = "engineer_db"


def create():
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS engineers(
            engineer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255)
        )    

    """)


def add(name, department):
    sql = "INSERT INTO engineers (name,department) VALUES (%s,%s)"
    val = [("abilash", "AI and ML"),
           ("avinash", "AI and ML"),
           ("PRAVEEN", "AI and ML"),
           ("harsha", "AI and ML"),
           ("mubarak", "CSE"),
           ("shivam shing", "CSE")]
    cursor.executemany(sql, val)
    connection.commit()


create()

add("name :", "department")

# cursor.execute("SELECT * FROM engineers")
# res = cursor.fetchall()
#
# for i in res:
#     print(i)
#




sql = "SELECT * FROM engineers WHERE department= %s"
cursor.execute(sql,('CSE',))
result = cursor.fetchall()
for i in result:
    print(i)
