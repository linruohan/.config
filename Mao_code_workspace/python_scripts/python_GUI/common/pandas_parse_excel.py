# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
# 使用pandas写入excel

import pandas as pd
from datetime import date, timedelta
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from scipy.stats import linregress
#显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# pd.options.display.max_columns = 77
# pd.options.display.max_rows=77
#设置数据的显示长度，默认为50
pd.set_option('max_colwidth',200)
#禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

import numpy as np
import seaborn as sns
import pyodbc
import sqlalchemy

class Excel:

    def __init__(self, path, sheetname="sheet1"):
        self.path = path
        self.sheetname = sheetname
        # self.df = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Time", "Pansen", "Liqin"]})
        # self.df = pd.read_excel(self.path, index_col="ID")
        self.df = pd.read_excel(self.path)  # 做数据校验用
        # print(self.df.sheet_names)

    def write(self, data):
        df = self.df.set_index('ID', inplace=True)  # 去掉index,并创建新对象
        df.to_excel("./output.xlsx")
        print("done")

    def read(self):
        people = pd.read_excel(self.path, header=1, index_col="ID")
        # header 1：从第二行读取 0：从第一行开始读取 None：没有表头,index_col:指定index，不自动生成
        people.columns = ["ID", "Type", "Title", "Firstname", "MiddleName", "Lastname"]
        print(people.shape)
        print(people.columns)
        print(people.head(3))
        print(people.tail(3))

    def row_col(self):
        """新增列"""
        s1 = pd.Series([1, 2, 3], index=["1", "2", "3"], name="A")
        s2 = pd.Series([10, 20, 300], index=["1", "2", "3"], name="B")
        s3 = pd.Series([100, 200, 300], index=["1", "2", "4"], name="C")
        df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # 常用添加方式
        print(df)

    def set_value(self, index, col, value):
        """设置值"""
        # for index in books.index:
        #     books.at[i,"ID"]=123
        #     books.at[i,"Price"]=123
        #     books.at[i,"Date"]=123
        self.df.at[index, col] = value

    def add_month(self, ori_date, add_month_num):
        """日期格式单元格.mouth+=增加月份"""
        add_year = add_month_num // 12
        new_month = ori_date.month + add_month_num % 12
        if new_month != 12:
            add_year += new_month // 12
            new_month = new_month % 12
        return date(ori_date.year + add_year, new_month, ori_date.day)

    def book(self):
        # books = pd.read_excel(self.path, skiprows=3, usecols="C:F", index_col=None)
        # skiprows=3从第四行开始读取 usecols="C:F" 使用C到F列
        books = pd.read_excel(self.path, index_col=None, dtype={"ID": str, "Price": str, "Date": str})
        books.set_index('ID')
        print(books["ID"].values)
        books["ID"].at[1] = "100"
        startdate = date(2018, 1, 1)
        for i in books.index:
            books["ID"].at[i] = i + 1
            books["Date"].at[i] = 'Yes' if i % 2 == 0 else "No"
            # =========== date 递增 ===========
            # 增加天数
            books['Date'].at[i] = startdate + timedelta(days=i)  # timedelta只可以设置时分秒和天，无法添加年和月
            # 增加年份
            books['Date'].at[i] = date(startdate.year + i, startdate.month, startdate.day)
            # 增加月份
            books['Date'].at[i] = self.add_month(startdate, i)
        books["Price"] = books["ListPrice"] * books["Discount"]
        books["ListPrice"] = books["ListPrice"].apply(lambda x: x + 2)
        print(books)

    def 多重排序(self):
        "先按照worthy顺序,再按照price逆序"
        products = pd.read_excel(self.path, index_col="ID")
        products.sort_values(by=["Worthy", "Price"], inplace=True, ascending=[True, False])

    def student_demo(self):
        student = self.df
        student = student.loc[student.Age.apply(lambda x: 18 <= x < 30)].loc[
            student.Score.apply(lambda x: 85 <= x <= 100)]
        print(student)

    def student_bar(self):
        """柱状图"""
        student = self.df
        student.sort_values(by="Score", inplace=True, ascending=False)
        # student.plot.bar(x="Field",y="Score",color="orange",title="Students by field")
        plt.bar(student.Field, student.Score, color='green')
        plt.xticks(student.Field, rotation="90")  # 旋转90度
        plt.xlabel('Field')
        plt.ylabel('Score')
        plt.title("tudents by field", fontsize=16)
        plt.tight_layout()  # 紧凑型布局
        plt.show()

    def student_bar2(self):
        """柱状图优化"""
        student = self.df
        student.sort_values(by="2017", inplace=True, ascending=False)
        student.plot.bar(x="Field", y=["2016", '2017'], color=["orange", 'red'], title="Students by field")
        plt.title("Students by field", fontsize=16, fontWeight='bold')
        plt.xlabel("Field", fontWeight='bold')
        plt.ylabel('Score', fontsize=12, fontWeight='bold')
        ax = plt.gca()  # 获取轴
        ax.set_xticklabels(student['Field'], rotation='45', ha='right')
        f = plt.gcf()  # figure 当前图形
        f.subplots_adjust(left=0.2, bottom=0.42)  # 调整左下边距
        plt.show()

    def 叠加水平柱状图(self):
        student = self.df
        student['Total'] = student['2016'] + student['2017'] + student['Score']
        student.sort_values(by='Total', inplace=True, ascending=True)
        # 垂直柱状图bar
        student.plot.bar(x="Field", y=['2016', '2017', 'Score'], stacked=True, title="Students by field")
        # 水平柱状图barh
        # student.plot.barh(x="Field",y=['2016','2017','Score'],stacked=True,title="Students by field")
        plt.tight_layout()
        plt.show()

    def 饼状图(self):
        student = self.df
        student['2017'].sort_values(ascending=True).plot.pie(fontsize='8', startangle=90)
        # student['2017'].plot.pie(fontsize='8',counterclock=False,startangle=90) # 简化写法不生效
        plt.title("Students of pie", fontsize='16', fontWeight='bold')
        plt.ylabel('2017', fontsize=12, fontWeight='bold')

    def 折线图(self):
        student = self.df
        student['Total'] = student['2016'] + student['2017'] + student['Score']

        print(student.columns)
        # 叠加折线图
        # student.plot(y=['Field', '2016', '2017', 'Age', 'Score'])
        # 叠加区域图
        student.plot.area(y=['Field', '2016', '2017', 'Age', 'Score'])
        # 叠加柱状图
        student.plot.bar(y=['Field', '2016', '2017', 'Age', 'Score'], stacked=True)
        plt.title("plt demo")
        plt.ylabel('Total', fontsize=12, fontWeight='bold')
        plt.xticks(student.index)
        plt.show()

    def 散点图(self):
        student = self.df
        print(student.corr())  # 打印每两列数据的相关性
        # 散点图
        # student.plot.scatter(x='Age',y='Score')
        # 直方图
        # student['2016'].plot.hist(bins=10)
        # 密度图
        student['2016'].plot.kde()
        plt.xticks(range(0, max(student['2016']), 500), fontSize=8)
        plt.show()

    def 多表联合查询(self):
        student = pd.read_excel(self.path, index_col="ID", sheet_name='student')
        mysheet = pd.read_excel(self.path, index_col="ID", sheet_name='mysheet')
        # table=student.merge(mysheet,how='left',on='ID').fillna(0)
        # table = student.merge(mysheet, how='left', left_on='ID', right_on="ID").fillna(0)
        table = student.join(mysheet, how='left', on='ID').fillna(0)
        table.Score = table.Score.astype(int)
        self.save(table, 'table')

    def 同时写多个sheet(self, dfs_dict):
        with pd.ExcelWriter(self.path) as writer:
            for df, sheet_name in dfs_dict.items():
                df.to_excel(writer, sheet_name=sheet_name)

    def save(self, df, sheetname):
        # pandas覆盖写多个sheet
        with pd.ExcelWriter(self.path) as writer:
            writer.book = load_workbook(self.path)
            writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
            df.to_excel(writer, sheetname, index=False)
        # table.to_excel(writer,sheet_name='table')
        # mysheet.to_excel(writer,sheet_name='mysheet')
        # student.to_excel(writer,sheet_name='student')

    def 数据格式校验(self):
        def score_validation(row):
            try:
                assert 0 < row.Score < 100
            except Exception:
                print(f"{row.ID} {row.Name} invalid value  {row.Score}")

        student = self.df
        student.apply(score_validation, axis=1)

    def 一列数据分割成两列(self):
        student = self.df
        string = student.Field.str.split(expand=True, n=1)
        student['first'] = string[0]
        student['second'] = string[1].str.upper()
        print(student)

    def 总分和平均(self):
        student = self.df
        scores = student[['ID', 'Score1', 'Score2', 'Score3']]
        row_sum = scores.sum(axis=1)
        row_mean = scores.mean(axis=1)
        student['row_sum'] = row_sum
        student['row_mean'] = row_mean
        col_mean = student[['ID', 'Score1', 'Score2', 'Score3', 'row_sum', 'row_mean']].mean()
        col_mean.ID = "Summary"
        scores = scores.append(col_mean, ignore_index=True)

        print(scores)

    def 去重(self):
        student = self.df
        # student.drop_duplicates(subset='Name',inplace=True,keep="first")# 保留前面的数据
        student.drop_duplicates(subset='Name', inplace=True, keep="last")  # 保留后面的数据
        dup = student.duplicated(subset='Name')  # 找出重复的数据
        print(dup.any())  # 是否有重复数据
        # dup=dup[dup==True]
        dup = dup[dup]  # 重复的数据index
        print(student.iloc[dup.index])  # 打印完整重复数据

    def 旋转行和列(self):
        student = pd.read_excel(self.path, index_col="ID")
        student = student.transpose()
        print(student)

    def import_other(self):
        df1 = pd.read_csv('1.csv', index_col="ID")
        df2 = pd.read_csv('1.tsv', sep='\t', index_col="ID")
        df3 = pd.read_csv('1.txt', sep=',', index_col="ID")

    def 透视表(self):
        df = self.df
        df['Year'] = pd.DatetimeIndex(df['Date']).year
        # 第一种方法:
        # pt1=df.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)
        # 第二种方法
        groups = df.groupby(['category', 'Year'])
        sum = groups['Total'].sum()
        count = groups['ID'].count()
        pt2 = pd.DataFrame({'Sum': sum, 'count': count})

    def 线性回归(self):
        """数据预测"""
        df = self.df
        slope, intercept, r, p, std_err = linregress(df.index, df.Revenue)
        exp = df.index * slope + intercept

        plt.scatter(df.index, df, Revenue)
        plt.plot(df.index, exp, color="red")
        plt.title("Sales")
        plt.xticks(df.index.df.Month, rotation=90)
        plt.tight_layout()
        plt.show()

    def 条件格式(self):
        def low_score_red(s):
            color = 'red' if s < 60 else 'black'
            return f'color:{color}'

        def hight_score_green(col):
            return ['background-color:line' if s == col.max() else 'background-color:white' for s in col]

        student = self.df

        student.style.applymap(low_score_red, subset=['Score1', 'Score2', 'Score3']).apply(hight_score_green,
                                                                                           subset=['Score1', 'Score2',
                                                                                                   'Score3'])
        # student.to_excel()
        self.save(student, 'student')
        print(student)

    def 颜色深浅和进度条(self):
        color_map = sns.light_palette("green", as_cmap=True)
        student = self.df
        # 背景颜色深浅
        student.style.background_gradient(color_map, subset=['Score1', 'Score2', 'Score3'])
        # 背景颜色进度条
        student.style.bar(color='red', subset=['Score1', 'Score2', 'Score3'])

    def 行操作(self):
        student1 = self.df
        student2 = self.df
        # 追加
        add = student1.append(student2).reset_index(drop=True)  # drop 放弃index
        std = pd.Series({'ID': 43, 'Name': 'xiaohan', 'Score': 99})
        add.append(std, ignore_index=True)
        # 修改
        student1.at[39, 'Name'] = 'xiaosd'
        student1.at[39, 'Score'] = 'xiaosd'
        # 替换
        std1 = pd.Series({'ID': 43, 'Name': 'xiaohan', 'Score': 99})
        student1.iloc[49] = stu1
        # 插入
        std1 = pd.Series({'ID': 43, 'Name': 'xiaohan', 'Score': 99})
        part1 = student[:20]
        part2 = student[20:]
        student = part1.append(std1, ignore_index=True).append(part2).reset_index(drop=True)
        # 删除
        student1.drop(index=[0, 1, 2], inplace=True)
        student1.drop(index=range(0, 10), inplace=True)  # 0-9行删除
        student1.drop(index=student1[0:10].index, inplace=True)  # 0-9行删除
        # 条件删除
        for i in range(5, 10):
            student1['Name'].at[i] = ''
        miss = student1.loc[students['Name'] == '']
        student1.drop(index=miss.index, inplace=True).reset_index(drop=True)

    def 列操作(self):
        student1 = self.df
        student2 = self.df
        students = pd.concat([student1, student2], axis=1).reset_index(drop=True)  # 两个表的列合并
        # 追加列
        students['Age'] = 23
        # students['Age']=np.repeat(25,len(students))
        # students['Age']=np.arange(0,len(students))
        # 删除列
        students.drop(columns=['Age', 'Score'], inplace=True)
        # 插入列
        students.insert(1, column='Foo', value=np.repeat("foo", len(students)))
        # 表头大写
        studen.rename(columns={'Foo': 'FOO', 'Name': "NAME"}, inplace=True)
        # 删除ID为NAN的行
        students['ID'] = students['ID'].astype(float)
        for i in range(5, 12):
            students['ID'].at[i] = np.nan
        students.dropna(inplace=True)  # 任意一列有NAN的行都会被删掉

    def 链接数据库(self):
        conn=pyodbc.connect('DRIVER={SQL Server};SERVER={local};DATABASE=AdventureWorks;USERS=sa;PASSWORD=123456')
        query='select * from Person.Person'
        df1=pd.read_sql_query(query,conn)
        print(df1.head())

        engine=sqlalchemy.create_engine('mssql+pyodbc://sa:123456@{local}/AdventureWorks?driver=SQL+Server')
        df2=pd.read_sql_query(query,engine)
        print(df2.head())
    def 长方形外接圆面积(self):
        rects=self.df
        def get_circumcircle_area(l,h):
            r=np.sqrt([l**2+h**2])/2
            return r**2*np.pi
        def wrapper(row):
            return get_circumcircle_area(row['Length'],row['Heghet'])
        rects['CA']=rects.apply(wrapper,axis=1)
        print(rects)




if __name__ == '__main__':
    path = "./data/Students.xlsx"
    excel = Excel(path)
    excel.条件格式()
