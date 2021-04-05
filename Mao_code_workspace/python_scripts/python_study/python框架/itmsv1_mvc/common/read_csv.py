import csv
path="csvData.csv"
def read(path):
    # 读取csv文件方式1
    with open (path, "r")as csvFile:
        reader = csv.reader (csvFile)  # 返回的是迭代类型
        data = []
        for item in reader:
            print (item)
            data.append (item)
        print (data)
    return data
def write(path,data):
    with open (path, 'w', newline='') as f: # 设置newline，否则两行之间会空一行
        writer = csv.writer (f, dialect='excel')
        header=['',]
        writer.writeheader(header)
        # writer.writerows(data)
        for i in range (len (data)):
            writer.writerow (data[i])
def read_dict(path):
    f=csv.reader(open(path,'r'))
    print (list (f))#打印所有数据
    # 读取一行，下面的reader中已经没有该行了
    head_row = next (f)#第一行是标题
    print(head_row)
    for row in f:
        # 行号从2开始
        print(f.line_num,row)
def write_from_dict(path,datas):
    # csv 写入
    headers = ['name', 'age']
    # datas = [{'name': 'Bob', 'age': 23}, {'name': 'Jerry', 'age': 44}, {'name': 'Tom', 'age': 15}]
    # 打开文件，追加a
    with open (path, 'a', newline='')as f:
        # 标头在这里传入，作为第一行数据
        writer = csv.DictWriter (f, headers)
        writer.writeheader ()
        # for row in reader:
        #     # Max TemperatureF是表第一行的某个数据，作为key
        #     max_temp = row['Max TemperatureF']
        # for row in datas:
        #     writer.writerow (row)
        # 还可以写入多行
        writer.writerows (datas)
if __name__ == '__main__':

    path='001.csv'
    write(path)
    read(path)
