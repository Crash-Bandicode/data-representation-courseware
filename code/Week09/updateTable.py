import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0831560551crash",
    database="datarepresentation"
)

cursor = db.cursor()
sql = "update student set name=%s, age=%s where id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql, values)

db.commit()
print("Update done")