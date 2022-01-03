import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0831560551crash",
    database="datarepresentation"
)

cursor = db.cursor()
sql = "delete from student where id =%s"
values = (1,)

cursor.execute(sql, values)

db.commit()
print("delete done")