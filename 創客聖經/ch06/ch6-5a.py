import pymysql

db = pymysql.connect(host="localhost",
                     user="pma",
                     password="a123456",
                     database="myschool",
                     charset="utf8")

cursor = db.cursor()
student = ["s111", "陳允東", "桃園市八德", "2000-07-01"]
sql = """INSERT INTO students (sno,name,address,birthday)
         VALUES ('{0}','{1}','{2}','{3}')"""
sql = sql.format(student[0], student[1], student[2], student[3])
print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("新增一筆記錄...")
except:
    db.rollback() 
    print("新增記錄失敗...")
db.close()
