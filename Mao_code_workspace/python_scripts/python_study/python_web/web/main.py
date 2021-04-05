import web
import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='12345',db='test',port=3306, cursorclass=MySQLdb.cursors.DictCursor)
cur = conn.cursor()
cur.execute('select * from user')
r = cur.fetchall()
cur.close()
conn.close()
print (r)
