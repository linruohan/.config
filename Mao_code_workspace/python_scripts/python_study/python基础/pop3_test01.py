#coding=utf-8
from email.parser import Parser
from email.header import  decode_header
from email.utils import parseaddr
import  poplib

#输入邮件地址、口令、和pop3服务器地址
email='**@163.com'
password='授权码'
pop3_server='smtp.163.com'
#连接到pop3服务器
server=poplib(pop3_server)
server.set_debuglevel(1)#打开或关闭调试信息
print(server.getwelcome().decode('utf-8'))#打印pop3服务器的欢迎文字
#身份认证
server.user(email)
server.pass_(password)

#stat（）返回邮件数量和占用的空间
print('Message:%s .Size: %s .' %server.stat())
#list()返回所有邮件的编号
resp,mails,octets=server.list()
#可以查看返回的列表类似[b'1 82923',b'2 2184'.....]
print(mails)

#获取最新一份邮件，注意索引从1开始
index=len(mails)
resp,lines,octets=server.retr(index)

#lines存储了邮件的原始文本的每一行
#可以获取整个邮件的原始文本
msg_content=b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件
msg=Parser().parsestr(msg_content)


#可以根据邮件index直接从服务器删除邮件
server.dele(index)
#关闭连接
server.quit()
