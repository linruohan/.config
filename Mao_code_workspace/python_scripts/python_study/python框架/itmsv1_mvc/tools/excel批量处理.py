import os
import numpy as np
import pandas as pd
import xlrd
print ('work_directory: ', os.getcwd ())
# path   sheet
loadfile_sheet = ['../exel/001test01.xls', '理事与会员名单']
# sheet中的列
common_columns = ['回执参加', '回执不参加']
# 相关列
concerned_columns = ['理事', '会员']

disp_columns = ['参会', '不参会', '未回执']
# 保存文件  sheet1  sheet2
savefile_sheet = ['../exel/001test.xls', '理事回执统计', '会员回执统计']


def disp(ss, cap, num=True):
    # 功能：显示名单
    # ss  : 名单集合
    # cap ：开头描述
    print (cap, '({})'.format (len (ss)))
    for i in range (np.ceil (len (ss) / 5).astype (int)):
        pre = i * 5
        nex = (i + 1) * 5
        # 调整显示格式
        dd = ''
        for each in list (ss)[pre:nex]:
            if len (each) == 2:
                dd = dd + '    ' + each
            elif len (each) == 3:
                dd = dd + '  ' + each
            else:
                dd = dd + '' + each
        print ('{:3.0f} -{:3.0f} {}'.format (i * 5 + 1, (i + 1) * 5, dd))


def trans_pd(df, ll, cap, i=1):
    # 功能：生成三列--空列、序号列、数据列
    # df  : DataFrame结构
    # ll  : 列表
    # cap : 显示的列名
    # i   : 控制空列的名字
    df['_' * i] = pd.DataFrame ([''])
    if len (set (ll)) == 1:
        df['序号{}'.format (i)] = np.NaN
        df[cap] = np.NaN
    else:
        df['序号{}'.format (i)] = pd.DataFrame (np.arange (len (set (ll)) - 1) + 1)
        df[cap] = pd.DataFrame (ll)
    return df


def prep(ss, N):
    # 功能：预处理，生成列表，并补齐到长度N
    # ss  : 集体
    # N   ：长度
    ll = list (ss)
    L = len (ll)
    ll.extend ([np.NaN] * (N - L))
    return ll


def get_df(loadfile_sheet):
    # 1. 载入excel
    data = pd.read_excel (loadfile_sheet[0], loadfile_sheet[1])
    # 4. 返回DataFrame
    df = pd.DataFrame (loadfile_sheet[0], columns=data.columns)
    return df


def save2excel(df, loadfile_sheet,sheetnew, savefile_sheet):
    idx = 0
    book = xlrd.open_workbook (loadfile_sheet[0])
    for i in book.sheet_names ():
        if sheetnew in i:
            idx = i
            break
    if idx != 0:  # 如果有对应sheet
        names = locals ()
        for i in range(len(book.sheet_names ())+1):
            if i != idx:
                names = pd.read_excel (savefile_sheet[0], sheet_name=savefile_sheet[i])
                print (names)
        writer = pd.ExcelWriter (savefile_sheet[0])
        for i in book.sheet_names ():
            if i != idx:
                names['df%s' % i].to_excel (writer, sheet_name=savefile_sheet[i])
                df.to_excel (writer, sheet_name=savefile_sheet[i])
        writer.save ()
    else:  # 如果没有对应sheet，创建一个新sheet
        names = locals ()
        names['df%s' % i] = pd.read_excel (savefile_sheet[0], sheet_name=savefile_sheet[i])
        writer = pd.ExcelWriter (savefile_sheet[0])
        names['df%s' % i].to_excel (writer, sheet_name=savefile_sheet[i])
        df.to_excel (writer, sheet_name=concerned_column)
        writer.save ()
    print ('writing success')


if __name__ == '__main__':
    for concerned_column in concerned_columns:
        df = get_df (loadfile_sheet, common_columns, concerned_column, disp_columns, display=True)
        save2excel (df, concerned_column, savefile_sheet)
