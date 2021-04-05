import MySQLdb

conn=MySQLdb.connect("localhost","root","12345","itis")
cur=conn.cursor()
sql="select * from jc_accident_map"
# name="xiaohan"
# insert_sql="insert into news(newstitle) values('%s')"%(name)

# cur.execute(insert_sql)
# conn.commit()
cur.execute(sql)
result=cur.fetchall()


for i in result:
    print(i)

conn.close()
