import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0831560551crash",
    #user ="codes"
    #passwd="passord"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")