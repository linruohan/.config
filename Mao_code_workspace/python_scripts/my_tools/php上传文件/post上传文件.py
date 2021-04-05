import requests
import os

url = 'http://www.test.com/doFile.php'
#url = 'http://www.test.com/doPost.php'
#files = {'file': open('D:/tmp/1.jpg', 'rb')}

# 要上传的文件
files = {'file123': ('1.jpg', open(os.path.dirname(__file__)+'/1.jpg', 'rb'))
         }  # 显式的设置文件名

# post携带的数据
data = {'a': '杨', 'b': 'hello'}


r = requests.post(url, files=files, data=data)
print(r.text)
with open(os.path.dirname(__file__)+'/1.html', 'w') as f:
    f.write(r.text)
