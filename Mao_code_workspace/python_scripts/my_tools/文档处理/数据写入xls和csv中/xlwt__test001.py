import xlwt
import xlrd
import xlutils
from xlutils.copy import copy

#init xls file（写新的文件并保存）
#styleBlueBkg= xlwt.easyxf('pattern: pattern solid, fore_colour sky_blue;');
#styleBold   = xlwt.easyxf('font: bold on');
styleBoldRed = xlwt.easyxf('font: color-index red, bold on');
headerStyle = styleBoldRed;
wb = xlwt.Workbook();
ws = wb.add_sheet('xiaohan');
ws.write(0, 0, "Header",        headerStyle);
ws.write(0, 1, "CatalogNumber", headerStyle);
ws.write(0, 2, "PartNumber",    headerStyle);
wb.save('123.xls');


#open existed xls file（复写，添加新的内容，重新保存）
oldWb = xlrd.open_workbook('123.xls', formatting_info=True)#保留原格式打开;
print (oldWb); #
newWb = copy(oldWb);#复制旧的文件
print (newWb);
newWs = newWb.get_sheet(0)#获取第一行数据;
newWs.write(1, 0, "value1");
newWs.write(1, 1, "value2");
newWs.write(1, 2, "value3");
print ("write new values ok");
newWb.save('123.xls');
print ("save with same name ok");
