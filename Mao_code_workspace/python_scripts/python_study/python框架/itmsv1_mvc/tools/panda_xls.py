import pandas as pd
import xlrd
import numpy as np

xlsfile = r'UITest.xls'
book = xlrd.open_workbook(xlsfile)
#xlrd用于获取每个sheet的sheetname
count = len(book.sheets())
print(count)
for i in book.sheet_names():
    print(i)
# with pd.ExcelWriter('newxls.xls') as writer:
#     for sheet in book.sheets():
#         # print (sheet.name)
#         df = pd.read_excel(xlsfile,sheet.name,index_col = None)
#         df1=df.replace(9999,np.nan).dropna(axis=0)
#         df2=df1.iloc[:,:2]
#         df3=df1.iloc[:,2]
#         #np.sin和np.cos按元素计算，好啊
#         df4=(-1)*np.sin(df3)*df1.iloc[:,3]
#         df5=(-1)*np.cos(df3)*df1.iloc[:,3]
#         #重新拼接
#         pieces=[df2,df4,df5]
#         df6=pd.concat(pieces,axis=1)
#         #对columns重新命名
#         column_index={'jingdu':'jingdu','weidu':'weidu',0:'u',1:'v'}
#         df7=df6.rename(columns=column_index)
#         #结果写入excel中的sheet
#         df7.to_excel(writer,sheet_name = sheet.name)