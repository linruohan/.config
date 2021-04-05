# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'


def read_sql_file(filename):
    with open(filename, 'r+') as f:
        # sql文件最后一行加上;
        sql_list = f.read().split(';')[:-1]
        # 将每段sql里的换行符改成空格
        sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
        return sql_list


docs = [
    # 1	sqlite3.connect(database [,timeout ,other optional arguments]) # 打开到SQLite 数据库文件 database的链接。(不存在就新建)
    # 2	connection.cursor([cursorClass])#创建一个 cursor
    # 3	cursor.execute(sql [, optional parameters])执行一个 SQL 语句,被参数化（即使用占位符代替 SQL 文本）占位符：问号和命名占位符（命名样式）例如：cursor.execute("insert into people values (?, ?)", (who, age))
    # 4	connection.execute(sql [, optional parameters])# 调用光标（cursor）方法创建了一个中间的光标对象，然后通过给定的参数调用光标的 execute 方法。
    # 5	cursor.executemany(sql, seq_of_parameters)#对 seq_of_parameters 中的所有参数或映射执行一个 SQL 命令
    # 6	connection.executemany(sql[, parameters])# 由调用光标（cursor）方法创建的中间的光标对象的快捷方式，然后通过给定的参数调用光标的 executemany 方法。
    # 7	cursor.executescript(sql_script)会#执行多个 SQL 语句。它首先执行 COMMIT 语句，然后执行作为参数传入的 SQL 脚本。所有的 SQL 语句应该用分号 ; 分隔
    # 8	connection.executescript(sql_script)# 该例程是一个由调用光标（cursor）方法创建的中间的光标对象的快捷方式，然后通过给定的参数调用光标的 executescript 方法。
    # 9	connection.total_changes()# 该例程返回自数据库连接打开以来被修改、插入或删除的数据库总行数。
    # 10	connection.commit()# 该方法提交当前的事务。如果您未调用该方法，那么自您上一次调用 commit() 以来所做的任何动作对其他数据库连接来说是不可见的。
    # 11	connection.rollback()# 该方法回滚自上一次调用 commit() 以来对数据库所做的更改。
    # 12	connection.close()# 该方法关闭数据库连接。请在此之前调用 commit()。否则更改将全部丢失！
    # 13	cursor.fetchone()# 该方法获取查询结果集中的下一行，返回一个单一的序列，当没有更多可用的数据时，则返回 None。
    # 14	cursor.fetchmany([size=cursor.arraysize])# 该方法获取查询结果集中的下一行组，返回一个列表。当没有更多的可用的行时，则返回一个空的列表。该方法尝试获取由 size 参数指定的尽可能多的行。
    # 15	cursor.fetchall()# 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
]
import sqlite3


class MySqliteDb:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('DB/test.db')
            self.cursor = self.conn.cursor()
            print("connect database successfully")
        except Exception as e:
            print(f"connect failed {e}")

    def create_table(self, create_table_sql_file='DB/test.sql'):
        sql_list = read_sql_file(create_table_sql_file)
        for sql_item in sql_list:
            self.cursor.execute(sql_item)
        print("Table created successfully")
        self.conn.commit()

    def insert(self, table="COMPANY", key_list=["ID", "NAME", "AGE", "ADDRESS", "SALARY"],
               value_tuple=(9, "'Maodou'", 30, "'California'", 20000.00)):
        # table='COMPANY'
        print(table, '123123')
        sql_str = "INSERT INTO " + table + " (" + ",".join(key_list) + ") VALUES (" + ",".join(
            map(str, value_tuple)) + ");"
        print(sql_str)
        # self.cursor.execute("INSERT INTO COMPANY (?,?,???) \
        #       VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        self.cursor.execute(sql_str)
        self.conn.commit()
        print("Records insert successfully")

    def select(self, table_name="COMPANY"):
        # SELECT 操作
        cursor = self.cursor.execute("SELECT id, name, address, salary  from " + table_name)
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3], "\n")
        self.conn.close()

    def update(self):
        # UPDATE 操作
        self.cursor.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
        self.conn.commit()
        print("Total number of rows updated :", self.conn.total_changes)
        cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3], "\n")

        print("Operation done successfully")

    def close(self):
        self.conn.close()

    def delete(self):
        # DELETE 操作
        self.cursor.execute("DELETE from COMPANY where ID=2;")
        self.conn.commit()
        print("Total number of rows deleted :", self.conn.total_changes)

        cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3], "\n")

        print("Operation done successfully")
        self.conn.close()


if __name__ == '__main__':
    db = MySqliteDb()
    # db.create_table()
    # db.insert()
    db.select()
