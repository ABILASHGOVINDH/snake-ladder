import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123abiMahesh",
    database = "testdb"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE student (name VARCHAR(255), age INTEGER(10)) ")
# mycursor.execute("SHOW DATABASES ")
# # mycursor.execute("SHOW TABLES ")
#
# for i in mycursor:
#     print(i)

# sqlFromula = "INSERT INTO student (name,age) VALUES(%s,%s)"
# # student1 = ("Mahesh",48)  # single use
# students = [("Mahesh",48),
#             ("abi",19),
#             ("avi",22),
#             ("govindh",54),
#             ("yogehs",23)]
# mycursor.executemany(sqlFromula, students)
#
# mydb.commit()
#
# mycursor.execute("SELECT age FROM student") # name and age can be viewed
# # result = mycursor.fetchall() # use fetchone() select or fetch one row
# result = mycursor.fetchone()
# for i in result:
#     print(i)

# #LIMIT CAN VIEW DATA(sequence) LIMIT VALUES
# sal = "SELECT * FROM student LIMIT 5"
# mycursor.execute(sal)
# result = mycursor.fetchall()
# for i in result:
#     print(i)
# #LIMIT OFFSET CAN VIEW DATA(sequence) LIMIT VALUES THAT SEQUENCE CAN BE FIXED
# sal = "SELECT * FROM student LIMIT 5 OFFSET 3"
# mycursor.execute(sal)
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# #ORDER BY
# sal ="SELECT * FROM student ORDER BY name DESC"
# mycursor.execute(sal)
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# # DELETE
# sal = "DELETE  FROM student WHERE name ='Mahesh'"
# mycursor.execute(sal)
# mydb.commit()

# # DROP
# sal = "DROP FORM TABLE"
# mycursor.execute()
# mydb.commit()

mycursor.close()
mydb.close()