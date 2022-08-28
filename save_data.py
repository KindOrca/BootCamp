import csv
import pymysql

conn = pymysql.connect(
    host='221.138.0.16',
    user='root',
    password='#dp5csv5serv',
    db='project_3',
    charset='utf8mb4',
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

cur = conn.cursor()

sql = "INSERT INTO no_show VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

f = open('No_show.csv','r', encoding='utf-8')
rd = csv.reader(f)
next(rd)
for line in rd:
    cur.execute(sql, (0, line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13]))

conn.commit()
conn.close()
f.close()