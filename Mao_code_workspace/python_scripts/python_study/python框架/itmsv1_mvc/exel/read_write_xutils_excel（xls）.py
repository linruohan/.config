import xlrd, xlwt
from xlutils.copy import copy

'''只可对xls和xlsx文件进行读和写操作，但是手动查看不了xlsx文件，会报文件格式错误'''
def read3():
    data = xlrd.open_workbook ('C:\\Users\\32065\\Desktop\\Net\\simulation\\excel\\test.xls')
    table = data.sheets ()[0]  # open the first sheet
    nrows = table.nrows  # not-null rows
    print(nrows)

    for i in range (nrows):  # print by rows
        if i == 0:  # 跳过第一行
            continue
        print(table.row_values (i)[0:2])

def read(path):
    '''
    book=xlrd.open_workbook（filename = None，logfile = <_ io.TextIOWrapper
    name ='<stdout>'mode ='w'encoding ='UTF-8'>，
    verbosity = 0，use_mmap = 1，file_contents = None，
    encoding_override = None，formatting_info = False，
    on_demand = False，ragged_rows = False ）

    sheet=book.sheet_by_name("")
    sheet=book.sheet_by_index(1)
    sheetnames=book.sheet_names（）
    isloaded=sheet_loaded（sheet_name_or_index ）(返回True或False)
    unload_sheet（sheet_name_or_index ）
    '''
    data = xlrd.open_workbook (path)

    table = data.sheets ()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    for i in range (0, nrows):
        rowValues = table.row_values (i)  # 某一行数据
        for item in rowValues:
            print (item)
def write(path,sheetname,data):
    # book.add_sheet（sheetname，cell_overwrite_ok = False ）
    # worksheet=xlwt.Worksheet.Worksheet（sheetname，parent_book，cell_overwrite_ok = False ）
    # style=xlwt.Style.easyxf（strg_to_parse = ''，num_format_str = None，field_sep = '，'，line_sep = ';'，intro_sep = '：'，esc_char = '\\'，debug = False ）
    # sheet.write（r，c，label = ''，style = < xlwt.Style.XFStyleobject > ）
    # book.save（filename_or_stream ）
    '''写excel文件'''
    wbk = xlwt.Workbook ()
    sheet = wbk.add_sheet (sheetname, cell_overwrite_ok=True)
    headList = ['标题1', '标题2', '标题3', '标题4', '总计']
    ldata = []
    num = [a for a in data]
    # for循环指定取出key值存入num中
    num.sort ()
    # 字典数据取出后无需，需要先排序
    for x in num:
        # for循环将data字典中的键和值分批的保存在ldata中
        t = [int (x)]
        for a in data[x]:
            t.append (a)
        ldata.append (t)
    for i, p in enumerate (ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate (p):
            # print(i, j, q)
            sheet.write (i, j, q)
    wbk.save (path)
def rewrite(path,sheetname,headers,data):
    rb = xlrd.open_workbook (path)
    sheetnames=rb.sheet_names()
    print(sheetnames)
    wb=copy(rb)
    if sheetname in sheetnames:
        index = [i for i in sheetnames if i == sheetname][0]
        ws = wb.get_sheet (index)
    else:
        ws = wb.add_sheet (sheetname, cell_overwrite_ok=True)
    for i in range (len (headers)):
        ws.write (0, i, headers[i])
    n = 0
    values = [(k, v) for row, values in data.items () for k, v in values.items ()]
    for i in range (len (data)):
        # if i == 15: break
        for j in range (len (headers)):
            k = [k for k, v in values]
            if k[j] == headers[j]:
                real = data[i][k[j]]
                ws.write (i + 1, j, real)
            j += 1
            n += 1
        i += 1
    wb.save (path)
def write_data(path,wb,ws,headers,data):
    for i in range (len (headers)):
        ws.write (0, i, headers[i])
    n = 0
    values = [(k, v) for row, values in data.items () for k, v in values.items ()]
    for i in range (len (data)):
        # if i == 15: break
        for j in range (len (headers)):
            k = [k for k, v in values]
            v = [v for k, v in values]
            # print(len(v))
            print(k[j],v[j])
            if k[j] == headers[j]:
                real = data[i][k[j]]
                print (real)
                # print (i+1, j,'v[j]==', v[j])
                # print ('*' * 50)
                ws.write (i + 1, j, real)
            j += 1
            n += 1
        i += 1
    wb.save (path)

data={
        0:{'张三1':'张三1','lisi1':'张23三1','hei':'张2三1'},
        1:{'张三1':'张三2','lisi1':'张12三1','hei':1002},
        2:{'张三1':'张三3','lisi1':'张321三1','hei':'张1三1'},
        }
print(data[1]['hei'])
headers = ['张三1', 'lisi1', 'hei', 'by', 'by_style', '二级定位']
# headers = ['模块', '页面元素', '标签', 'by', 'by_style', '二级定位']
# write('testre.xlsx','1223',data)
# read('testre.xlsx')
rewrite('testre.xlsx','10222',headers,data)