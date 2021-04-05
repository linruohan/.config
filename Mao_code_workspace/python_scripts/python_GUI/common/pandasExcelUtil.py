# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import time

import pandas as pd
from openpyxl import load_workbook
import sys,os
sys.path.append(os.path.dirname(__FILE__))



# 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def timeit(fun):
    def inner(*args, **kwargs):
        start_time = time.time()
        fun(*args, **kwargs)
        end_time = time.time()
        print('运行时间为:%.6f' % (end_time - start_time))

    return inner


class PandasExcel:
    def __init__(self, file_name, sheet_name, **kwargs):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.df = pd.read_excel(self.file_name, sheet_name=self.sheet_name, keep_default_na=False, header=0, names=None,
                                index_col=None,
                                **kwargs)

        # datetime_format='mmm d yyyy hh:mm:ss',
        # date_format='mmmm dd yyyy'
        # name:如果没有表头, 可用此参数传入列表做表头
        # header:指定数据表的表头,默认值为0, 即将第一行作为表头
        # skiprows=3,
        # index_col:用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。一般可以设定index_col=False指的是pandas不适用第一列作为行索引。
        # usecols：读取指定的列, 也可以通过名字或索引值
        self.df.fillna('')

    def get_sheet_names(self):
        """获取excel的所有sheet名"""
        return pd.ExcelFile(self.file_name).sheet_names

    def rename_col(self, old_name, new_name):
        """重命名列名"""
        self.df.rename(columns={old_name: new_name}, inplace=True)

    def date_convert(self, col_name):
        """日期列转换为日期格式"""
        return pd.to_datetime(self.df[col_name])

    def get_columns(self):
        """获取列名，既列索引的值"""
        # 第一行 列标题
        return self.df.columns.values.tolist()

    def get_indexes(self):
        """获取行名，既行索引的值"""
        # 第一列 行标题
        return self.df.index.values.tolist()

    def get_dtypes(self):
        """查看各列数据类型"""
        return self.df.dtypes

    def get_row(self, row_index):
        """获取某一行"""
        # return self.df.loc[row_index].values.tolist()
        return self.df.iloc[row_index].values.tolist()

    def get_col(self, col_name):
        """获取某一列"""
        return self.df[col_name].values.tolist()

    def get_cell(self, row_index, col_index):
        """获取[row_index,col_index]所在位置的单元格值，索引均从0开始"""
        return self.df.iloc[row_index, col_index]

    def save(self, sheet_name, save_data):
        """保存数据"""
        # self.df.to_excel(self.file_name, sheet_name=self.sheet_name, index=False, header=True)
        # 保存新的数据
        book = load_workbook(self.file_name)
        writer = pd.ExcelWriter(self.file_name, engine='openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        # 设置各列的样式
        # 虽然Pandas的Styler样式还包括设置显示格式、条形图等功能，但写入到excel却无效，所以我们只能借助Pandas的Styler实现作色的功能，而且只能对数据着色，不能对表头作色
        # save_data = save_data.style.applymap(lambda x: 'color:red', subset=["包名"]) \
        #     .applymap(lambda x: 'color:green', subset=["状态"]) \
        #     .applymap(lambda x: 'background-color:#ADD8E6', subset=["匹配"]) \
        #     .background_gradient(cmap="PuBu", low=0, high=0.5, subset=["领域"])
        save_data.to_excel(writer, sheet_name, index=False)
        writer.save()

    def insert_col(self, col_index, add_col_name, add_col_data):
        self.df.insert(col_index, add_col_name, add_col_data)
        self.save(self.sheet_name, self.df)

    def change_col_index(self, new_col_index, new_col_name, col_name):
        """将指定列 移动到新的位置上，并给新的列名"""
        # 改变某一列的位置。如：先删除A列，然后在原表data中第1列插入被删掉的列。
        self.df.insert(new_col_index, new_col_name, self.df.pop(col_name))

    def add_row(self, row_index, row_data_list):
        """添加一行  Index 从零开始"""
        # 2. 用loc指定位置添加一行df.loc[2]=[9,10,11,12]
        self.df.loc[row_index] = row_data_list
        # 按E列排序,并重置行索引
        # df1 = self.df.sort_values(by='E')
        # df2=df1.reset_index()
        # del df2['index']  # 删除掉原来的索引列index
        self.save(self.sheet_name, self.df)

    def add_row_by_row_name(self, row_name, row_data_list):
        """行索引不为数字，添加一行到特定位置"""
        if row_name and row_name in self.get_indexes():
            self.df.loc[row_name] = row_data_list
            self.save(self.sheet_name, self.df)

    def append_row(self, row_data_list):
        """ 字典方式添加一行，append，忽略索引"""
        row_data = dict(zip(self.get_columns(), row_data_list))
        self.df.append(row_data, ignore_index=True)
        self.save(self.sheet_name, self.df)

    def del_row(self):
        """删除一行数据"""
        # drop(self, labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors="raise" )
        # 删除列axis为1，当删除行axis为0
        # 删除第3,4行，这里下标以0开始，并且标题行不算在类, axis用法同上
        self.df = self.df.drop([2, 3], axis=0, inplace=True)
        print(self.df)

    def del_col(self, col_name):
        """删除一列数据"""
        self.df.drop(col_name, axis=1, inplace=True)  # 删除`属性1`列

    def remap_col_value_by_dict(self, col_name, map_dict):
        """把数据集中gender列的男替换为1，女替换为0，"""
        # ①使用字典进行映射
        self.df["gender"] = self.df["gender"].map({"男": 1, "女": 0})
        self.df[col_name] = self.df[col_name].map(map_dict)

    def remap_col_value_by_func(self, col_name, func):
        """把数据集中gender列的男替换为1，女替换为0，"""

        # ②使用函数
        def gender_map(x):
            gender = 1 if x == "男" else 0
            return gender

        # 注意这里传入的是函数名，不带括号
        self.df["gender"] = self.df["gender"].map(gender_map)
        self.df[col_name] = self.df[col_name].map(func)


def parse_data(file_path, sheet_name, base_file_path, base_sheet_name):
    base_excel = PandasExcel(base_file_path, base_sheet_name, usecols=['匹配', '状态', '包名', 'owner', '领域'])
    base_df = base_excel.df
    parse_excel = PandasExcel(file_path, sheet_name)
    parse_df = parse_excel.df
    base_df['union'] = base_df['包名'] + " " + base_df['匹配']
    parse_df['union'] = parse_df['包名'] + " " + parse_df['匹配']
    union_list = base_df['union'].values.tolist()
    for record_idx, record_str in parse_df['union'].iteritems():
        if record_str in union_list:
            parse_df['状态'].at[record_idx] = base_df['状态'][base_df['union'] == record_str].values[0]
            parse_df['owner'].at[record_idx] = \
                base_df['owner'][base_df['union'] == record_str].values[0]
            parse_df['领域'].at[record_idx] = base_df['领域'][base_df['union'] == record_str].values[0]
    parse_excel.del_col('union')
    parse_excel.save(parse_excel.sheet_name, parse_df)


def parse_data1(file_path, sheet_name, base_file_path, base_sheet_name):
    base_excel = PandasExcel(base_file_path, base_sheet_name, usecols=['匹配', '状态', '包名', 'owner', '领域'])
    base_df = base_excel.df
    parse_excel = PandasExcel(file_path, sheet_name)
    parse_df = parse_excel.df
    base_df['union'] = base_df['包名'] + " " + base_df['匹配']
    parse_df['union'] = parse_df['包名'] + " " + parse_df['匹配']
    result_df = parse_df.merge(base_df, on='union', how='left').fillna('')
    result_df.rename(
        columns={
            '匹配_x': '匹配',
            '包名_x': '包名',
            '状态_y': '状态',
            'owner_y': 'owner',
            '领域_y': '领域',
        },
        inplace=True)

    for no_use in ['状态_x', 'owner_x', '领域_x', 'union', '包名_y', '匹配_y']:
        result_df.drop(no_use, axis=1, inplace=True)
    # result_df.to_excel('001.xlsx', index=False)
    parse_excel.save(parse_excel.sheet_name, result_df)
    print("parse success !")


if __name__ == '__main__':
    start = time.time()
    parse_data1('./data1.xlsx', 'Sheet1', '基线.xlsx', 'Sheet1')
    print('共计耗时%.2f s' % (time.time() - start))
