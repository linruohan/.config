import os, sys, csv, xdrlib, xlrd, json
import natsort

class data_center:
    def __init__(self):
        # Default File Path:
        self.date_dir = os.getenv ('G_DATACENTER', 'E:\\atom\\robotFramework\\common\\resources')
        self.curr_dir = os.getenv ('G_CURRENTLOG', 'E:\atom\robotFramework\\logs')
    def Read_Data_From_Excel(self, filename, path=None, includeEmptyCells=True):

        if path == None:
            file = os.path.join (self.data_dir, filename)  # Default File Path
        else:
            file = os.path.join (path, filename)
        try:
            data = xlrd.open_workbook (file)
            table = data.sheets ()[0]

            nrows = table.nrows
            nclos = table.ncols

            listAll = []
            for row in range (2, nrows):
                alist = []
                for col in range (1, nclos):
                    val = table.cell (row, col).value
                    # Solve issue that get integer data from Excel file would be auto-changed to float type.
                    alist.append (self.keep_integer_type_from_excel (val))
                listAll.append (alist)
            # print listAll
            listAll = self.unic (listAll)
        except Exception as e:
            print(str (e))

        if includeEmptyCells is True:
            return listAll
        else:
            newList = []
            for element in listAll:
                while "" in element:
                    element.remove ("")
                newList.append (natsort.natsorted (element))
            OrderedData = natsort.natsorted (newList)
            return OrderedData

    def Read_Excel_File(self, filename, path=None, includeEmptyCells=True):

        if path == None:
            file = os.path.join (self.data_dir, filename)  # Default File Path
        else:
            file = os.path.join (path, filename)
        try:
            data = xlrd.open_workbook (file)
            table = data.sheets ()[0]

            nrows = table.nrows
            nclos = table.ncols

            listAll = []
            for row in range (2, nrows):
                for col in range (1, nclos):
                    val = table.cell (row, col).value
                    # Solve issue that get integer data from Excel file would be auto-changed to float type.
                    value = self.keep_integer_type_from_excel (val)
                    # print value, type(value)
                    listAll.append (value)
            # print listAll
            listAll = self.unic (listAll)
        except Exception as  e:
            print(str (e))

        if includeEmptyCells is True:
            return listAll
        else:
            # Delete all empty data
            while '' in listAll:
                listAll.remove ('')
            return listAll

    def Read_CSV_File(self, filename, path=None):
        if path == None:
            file = os.path.join (self.data_dir, filename)  # Default File Path
        else:
            file = os.path.join (path, filename)
        data = []

        with open (file, 'rb') as csvfile:
            data = [each for each in csv.DictReader (csvfile)]
            # reader =csv.reader(csvfile)
            # for col in reader:
            #   data.append(col)
            return self.unic (data)

    def is_number(self, val):
        # Check if value is number not str.
        try:
            float (val)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric (val)
            return True
        except (TypeError, ValueError):
            pass

    def keep_integer_type_from_excel(self, value):
        # Keep integer number as integer type. When reading from excel it has been changed to float type.
        if self.is_number (value) and type (value) != str and value % 1 == 0:
            return str (int (value))
        else:
            return value

    def unic(self, item):
        # Resolved Chinese mess code.
        try:
            item = json.dumps (item, ensure_ascii=False, encoding='cp936')
        except UnicodeDecodeError:
            try:
                item = json.dumps (item, ensure_ascii=False, encoding='cp936')
            except:
                pass
        except:
            pass

        item = json.loads (item, encoding='cp936')  # Convert json data string back
        return item

    def Read_Column_From_Excel(self, filename, column, path=None, includeEmptyCells=True):

        alist = []
        if path == None:
            file = os.path.join (self.data_dir, filename)  # Default Data Directory
        else:
            file = os.path.join (path, filename)

        try:
            excel_data = xlrd.open_workbook (file)
            table = excel_data.sheets ()[0]

            for row_index in range (2, table.nrows):
                value = table.cell (row_index, int (column)).value
                print (value)
                alist.append (self.keep_integer_type_from_excel (value))
            # print alist
            listAll = self.unic (alist)
        except Exception as e:
            print (str (e))

        if includeEmptyCells is True:
            return listAll
        else:
            # Delete all empty data
            while '' in listAll:
                listAll.remove ('')
            return listAll

    def Get_Sheet_Values_From_Excel(self, filename, sheetname, path=None, includeEmptyCells=True):

        if path == None:
            file = os.path.join (self.data_dir, filename)  # Default Data Directory
        else:
            file = os.path.join (path, filename)

        try:
            excel_data = xlrd.open_workbook (file)
            sheetNames = self.get_sheet_names (excel_data)
            my_sheet_index = sheetNames.index (sheetname)
            # print my_sheet_index
            table = excel_data.sheet_by_index (my_sheet_index)

            nrows = table.nrows
            nclos = table.ncols

            listAll = []
            for row in range (2, nrows):
                alist = []
                for col in range (1, nclos):
                    val = table.cell (row, col).value
                    # Solve issue that get integer data from Excel file would be auto-changed to float type.
                    alist.append (self.keep_integer_type_from_excel (val))
                listAll.append (alist)
            # print listAll
            listAll = self.unic (listAll)
        except Exception as e:
            print (str (e))

        if includeEmptyCells is True:
            return listAll
        else:
            newList = []
            for element in listAll:
                while "" in element:
                    element.remove ("")
                newList.append (natsort.natsorted (element))
            OrderedData = natsort.natsorted (newList)
            return OrderedData

    def get_sheet_names(self, wb):
        sheetNames = wb.sheet_names ()
        return sheetNames
