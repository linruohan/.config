import sqlite3
#连接到sqlite3数据库
#数据库文件时test.db，如果不存在，会自动创建（在当前目录）

conn=sqlite3.connect('test.db')
#创建一个cursor游标，通过他执行sql语句
cursor=conn.cursor()
#执行一条sql 语句，创建user表格
# cursor.execute('create table user(id varchar2(20) primary key,name varchar2(20))')
# cursor.execute('insert into user(id,name) values(\'1\',\'Michael\')')


cursor.execute('select * from user where id=?',('1',))
# 使用Cursor对象执行select语句时，
# 通过featchall()可以拿到结果集。结果集是一个list，
# 每个元素都是一个tuple，对应一行记录
values=cursor.fetchall()
print(values)
#rowcount返回影响的行数
print(cursor.rowcount)


#关闭cursor
cursor.close()
#提交事务
# conn.commit()

#关闭conn
conn.close()
