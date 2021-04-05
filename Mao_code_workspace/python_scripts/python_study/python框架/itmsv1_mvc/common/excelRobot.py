import os
import natsort
from operator import itemgetter
from datetime import datetime, timedelta
from xlrd import open_workbook, cellname, xldate_as_tuple, \
    XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_TEXT, XL_CELL_BOOLEAN, \
    XL_CELL_ERROR, XL_CELL_BLANK, XL_CELL_EMPTY, error_text_from_code
from xlwt import easyxf, Workbook
from xlutils.copy import copy as copy
'''xlutils.copy覆盖写文件只能是xls文件，xlxs文件不支持'''
class MyExcel:
    def __init__(self):
        self.wb = None#workbook
        self.tb = None
        self.sheetNum = None
        self.sheetNames = None
        self.fileName = None
        if os.name is "nt":
            self.tmpDir = "Temp"
        else:
            self.tmpDir = "tmp"

    def open_excel(self, filename, useTempDir=False):
        '''打开所有路径下的xls文件'''
        if useTempDir is True:
            print('Opening file at %s' % filename)
            self.wb = open_workbook(os.path.join("/", self.tmpDir, filename), formatting_info=False, on_demand=True)
        else:
            self.wb = open_workbook(filename, formatting_info=False, on_demand=True)
        self.fileName = filename
        self.sheetNames = self.wb.sheet_names()

    def open_excel_current_directory(self, filename):
        '''打开当前路径下的xls文件'''
        workdir = os.getcwd()
        print('Opening file at %s' % filename)
        self.wb = open_workbook(os.path.join(workdir, filename), formatting_info=False, on_demand=True)
        self.sheetNames = self.wb.sheet_names()

    def get_sheet_names(self):
        '''获取sheetnames'''
        sheetNames = self.wb.sheet_names()
        return sheetNames

    def get_number_of_sheets(self):
        '''获取sheetnames数量'''
        sheetNum = self.wb.nsheets
        return sheetNum

    def get_column_count(self, sheetname):
        '''获取列数'''
        sheet = self.wb.sheet_by_name(sheetname)
        return sheet.ncols

    def get_row_count(self, sheetname):
        '''获取行数'''
        sheet = self.wb.sheet_by_name(sheetname)
        return sheet.nrows

    def get_column_values(self, sheetname, column, includeEmptyCells=True):
        '''获取某列的数据'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        data = {}
        for row_index in range(sheet.nrows):
            cell = cellname(row_index, int(column))
            value = sheet.cell(row_index, int(column)).value
            data[cell] = value
        if includeEmptyCells is True:
            sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return sortedData
        else:
            data = dict([(k, v) for (k, v) in data.items() if v])
            OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return OrderedData

    def get_row_values(self, sheetname, row, includeEmptyCells=True):
        '''获取某行的数据'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        data = {}
        for col_index in range(sheet.ncols):
            cell = cellname(int(row), col_index)
            value = sheet.cell(int(row), col_index).value
            data[cell] = value
        if includeEmptyCells is True:
            sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return sortedData
        else:
            data = dict([(k, v) for (k, v) in data.items() if v])
            OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return OrderedData

    def get_sheet_values(self, sheetname, includeEmptyCells=True):
        '''获取某工作表sheet的数据'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        data = {}
        for row_index in range(sheet.nrows):
            for col_index in range(sheet.ncols):
                cell = cellname(row_index, col_index)
                value = sheet.cell(row_index, col_index).value
                data[cell] = value
        if includeEmptyCells is True:
            sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return sortedData
        else:
            data = dict([(k, v) for (k, v) in data.items() if v])
            OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
            return OrderedData

    def get_workbook_values(self, includeEmptyCells=True):
        '''获取整个Excel的数据【包括所有sheet】'''
        sheetData = []
        workbookData = []
        for sheet_name in self.sheetNames:
            if includeEmptyCells is True:
                sheetData = self.get_sheet_values(sheet_name)
            else:
                sheetData = self.get_sheet_values(sheet_name, False)
            sheetData.insert(0, sheet_name)
            workbookData.append(sheetData)
        return workbookData

    def read_cell_data_by_name(self, sheetname, cell_name):
        '''根据单元格名称获取数据如：E8，F6等'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        cellValue=''
        for row_index in range(sheet.nrows):
            for col_index in range(sheet.ncols):
                cell = cellname(row_index, col_index)
                if cell_name == cell:
                    cellValue = sheet.cell(row_index, col_index).value
        return cellValue

    def read_cell_data_by_coordinates(self, sheetname, column, row):
        '''根据坐标获取数据，row，column'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        cellValue = sheet.cell(int(row), int(column)).value
        return cellValue

    def check_cell_type(self, sheetname, column, row):
        '''检查单元格类型'''
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
        if cell.ctype is XL_CELL_NUMBER:
            print("The cell value is a number")
        elif cell.ctype is XL_CELL_TEXT:
            print("The cell value is a string")
        elif cell.ctype is XL_CELL_DATE:
            print("The cell value is a date")
        elif cell.ctype is XL_CELL_BOOLEAN:
            print("The cell value is a boolean operator")
        elif cell.ctype is XL_CELL_ERROR:
            print("The cell value has an error")
        elif cell.ctype is XL_CELL_BLANK:
            print("The cell value is blank")
        elif cell.ctype is XL_CELL_EMPTY:
            print("The cell value is empty")
        else:
            print(error_text_from_code[sheet.cell(row, column).value])

    def put_number_to_cell(self, sheetname, column, row, value):
        '''修改【数字】固定单元格的值并保存'''
        if self.wb:
            my_sheet_index = self.sheetNames.index(sheetname)
            cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
            if cell.ctype is XL_CELL_NUMBER:
                self.wb.sheets()
                if not self.tb:
                    self.tb = copy(self.wb)
        if self.tb:
            plain = easyxf('')
            sel.tb.get_sheet(my_sheet_index).write(int(row), int(column), float(value), plain)

    def put_string_to_cell(self, sheetname, column, row, value):
        '''修改【string】固定单元格的值并保存'''
        if self.wb:
            my_sheet_index = self.sheetNames.index(sheetname)
            cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
            if cell.ctype is XL_CELL_TEXT:
                self.wb.sheets()
                if not self.tb:
                    self.tb = copy(self.wb)
        if self.tb:
            plain = easyxf('')
            self.tb.get_sheet(my_sheet_index).write(int(row), int(column), value, plain)

    def put_date_to_cell(self, sheetname, column, row, value):
        '''修改【日期】固定单元格的值并保存'''
        if self.wb:
            my_sheet_index = self.sheetNames.index(sheetname)
            cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
            if cell.ctype is XL_CELL_DATE:
                self.wb.sheets()
                if not self.tb:
                    self.tb = copy(self.wb)
        if self.tb:
            print(value)
            dt = value.split('.')
            dti = [int(dt[2]), int(dt[1]), int(dt[0])]
            print(dt, dti)
            ymd = datetime(*dti)
            plain = easyxf('', num_format_str='d.M.yyyy')
            self.tb.get_sheet(my_sheet_index).write(int(row), int(column), ymd, plain)

    def modify_cell_with(self, sheetname, column, row, op, val):
        '''修改固定单元格的值进行op操作val后并保存，如：（0,0）*50'''
        my_sheet_index = self.sheetNames.index(sheetname)
        cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
        curval = cell.value
        if cell.ctype is XL_CELL_NUMBER:
            self.wb.sheets()
            if not self.tb:
                self.tb = copy(self.wb)
            plain = easyxf('')
            modexpr = str(curval) + op + val
            self.tb.get_sheet(my_sheet_index).write(int(row), int(column), eval(modexpr), plain)

    def add_to_date(self, sheetname, column, row, numdays):
        '''将单元格中日期添加固定天数numdays'''
        my_sheet_index = self.sheetNames.index(sheetname)
        cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
        if cell.ctype is XL_CELL_DATE:
            self.wb.sheets()
            if not self.tb:
                self.tb = copy(self.wb)
            curval = datetime(*xldate_as_tuple(cell.value, self.wb.datemode))
            newval = curval + timedelta(int(numdays))
            plain = easyxf('', num_format_str='d.M.yyyy')
            self.tb.get_sheet(my_sheet_index).write(int(row), int(column), newval, plain)

    def subtract_from_date(self, sheetname, column, row, numdays):
        ''' 将单元格中日期减去固定天数numdays'''
        my_sheet_index = self.sheetNames.index(sheetname)
        cell = self.wb.get_sheet(my_sheet_index).cell(int(row), int(column))
        if cell.ctype is XL_CELL_DATE:
            self.wb.sheets()
            if not self.tb:
                self.tb = copy(self.wb)
            curval = datetime(*xldate_as_tuple(cell.value, self.wb.datemode))
            newval = curval - timedelta(int(numdays))
            plain = easyxf('', num_format_str='d.M.yyyy')
            self.tb.get_sheet(my_sheet_index).write(int(row), int(column), newval, plain)

    def save_excel(self, filename, useTempDir=False):
        '''保存Excel'''
        if useTempDir is True:
            print('*DEBUG* Got fname %s' % filename)
            self.tb.save(os.path.join("/", self.tmpDir, filename))
        else:
            self.tb.save(filename)

    def save_excel_current_directory(self, filename):
        '''保存当前路径下的Excel'''
        workdir = os.getcwd()
        print('*DEBUG* Got fname %s' % filename)
        self.tb.save(os.path.join(workdir, filename))

    def add_new_sheet(self, newsheetname):
        '''保存新工作表'''
        self.tb = copy(self.wb)
        self.tb.add_sheet(newsheetname)

    def create_excel_workbook(self, newsheetname):
        # 添加新的工作表
        self.tb = Workbook()
        self.tb.add_sheet(newsheetname)
if __name__ == '__main__':
    s=MyExcel()
    # path = '../exel/001.xlsx'
    path = '001.xlsx'
    s.open_excel(path,useTempDir=False)
    f1=s.read_cell_data_by_name('PageElements','B2')
    print(f1)
