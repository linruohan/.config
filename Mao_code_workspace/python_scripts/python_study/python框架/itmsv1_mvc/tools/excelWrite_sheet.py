import pandas as pd
import xlrd, xlwt, sys, glob, os
from xlutils.copy import copy


def write_sheet(path, name):
    df = pd.read_excel (path, name)
    list_sheet = []
    for number in range (0, len (df)):
        print(number)
        for i in df[0:].iloc[number]:
            print (i)
            list_sheet.append (str (i))

    book = xlrd.open_workbook (path)
    list_sheet = book.sheet_names ()
    # print (list_sheet)


def set_excel(path, sheet_list):
    i = 0
    for name in sheet_list:
        if i == 0:
            book = xlwt.Workbook ()
            book.add_sheet (name)
            book.save (path)
            i = i + 1
        else:
            src = xlrd.open_workbook (path, formatting_info=True)
            destination = copy (src)
            destination.add_sheet (name)
            destination.save (path)



# def main():
#     path = 'UITest.xls'
#     sheet_list = xlrd.open_workbook (path).sheet_names ()
#     set_excel ('UITest.xls', sheet_list)
#     for name in sheet_list:
#         index = sheet_list.index (name)
#         write_sheet (path, name)
#         print ("##########")


if __name__ == "__main__":
    path = 'UITest.xls'  #
    sheet_list = xlrd.open_workbook (path).sheet_names ()
    # print(sheet_list)
    for name in sheet_list:
        write_sheet (path, name)
