import pymysql

db = pymysql.connect(host="localhost",
                     user="pma",
                     password="a123456",
                     database="myschool",
                     charset="utf8")

cursor = db.cursor()
sql = "SELECT * FROM students WHERE birthday <=%s"
cursor.execute(sql, "1992/08/09")

row = cursor.fetchone()
print(row[0], row[1])
print("-------------------------")
data = cursor.fetchall()
for row in data:
    print(row[0], row[1])
db.close()
