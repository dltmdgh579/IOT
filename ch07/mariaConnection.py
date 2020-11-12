import pymysql

db= pymysql.connect(host='localhost',user='root',password='159159',db='Incheonnational',charset='utf8')

cur = db.cursor()

cur.execute("SELECT * FROM student")

rows = cur.fetchall()
print(rows)

db.close()