# -*- coding: utf-8 -*-
import os;
from win32com.client import Dispatch;
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#from win32com.client import *;
"""
Python中处理操作Excel中的图表（Chart，Graph）
"""
def excelChart():
    xl = Dispatch("Excel.Application");
    #xl = win32com.client.Dispatch("Excel.Application")
    print ("xl=",xl);
    #[5] OK
    # xlsPath = "chart_demo.xls";
    # absPath = os.path.abspath(xlsPath);
    # print ("absPath=",absPath);
    # wb = xl.Workbooks.open(absPath); #OK
    #[6] OK
    rawPath = r"E:\atom\chart_demo.xlsx";
    wb = xl.Workbooks.open(rawPath); # OK

    xl.Visible = 1;
    ws = wb.Worksheets(1);
    ws.Range('$A1:$D1').Value = ['NAME', 'PLACE', 'RANK', 'PRICE'];
    ws.Range('$A2:$D2').Value = ['Foo', 'Fooland', 1, 100];
    ws.Range('$A3:$D3').Value = ['Bar', 'Barland', 2, 75];
    ws.Range('$A4:$D4').Value = ['Stuff', 'Stuffland', 3, 50];
    wb.Save();#保存数据
    wb.Charts.Add();#添加报表
    wc1 = wb.Charts(1);#实例化并加入数据

if __name__ == "__main__":
    excelChart();
