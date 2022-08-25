import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="123456",db="nuguna", charset="utf8")

curs = conn.cursor()
sql = "select * from userinfo"
curs.execute(sql)

rows = curs.fetchall()

print(rows)

for row in rows:
    print(row[1],row[2])


conn.close()