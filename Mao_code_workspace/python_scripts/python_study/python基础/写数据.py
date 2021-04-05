#coding=utf-8

import codecs

list = ['{"PN":"34VT123","DUID":"XXXX","location":{"coordinates":[-100.35256443,33.4586858]},"SPD":125,"DT":"2017-06-02T13:15:20Z","driverID":"XXXXX","cate":"event","subCate":"OBDII","eventOBDII":{"what":"emergencyBrake","param":2,"GID":123456479}}','{"PN":"34VT123","DUID":"XXXX","location":{"coordinates":[-100.35256443,33.4586858]},"SPD":125,"DT":"2017-06-03T13:15:20Z","driverID":"XXXXX","cate":"event","subCate":"OBDII","eventOBDII":{"what":"emergencyBrake","param":2,"GID":123456479}}']
f = codecs.open("main.txt",'w','utf-8')


#f.write(str(list))
for i in list:
    f.write(str(i)+'\n')  #\n为换行符

f.close()

# list1 = [[1,2],[3,4]]
#
# s = u'亚像素精度：\r\n'  #u表示读取中文，\r\n为换行符
# f1 = codecs.open("main.txt",'w','utf-8')
#
# f1.write(s)
# #f.write(str(list))
# for i in list1:
#     f1.write(str(i)+'\r\n')  #\r\n为换行符
#
# f1.close()
