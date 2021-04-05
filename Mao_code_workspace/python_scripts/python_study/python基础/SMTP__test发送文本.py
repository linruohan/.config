#coding=utf-8

from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr

# 
# http_proxy='32.32.32.32:808'
# https_proxy='32.32.32.32:808'
#格式处理
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


# from_addr='mjt1220@126.com'
# to_addr='1214875764@qq.com'
# smtp_server='smtp.126.com'
# passwd='Mm1214875764'    #授权码

from_addr='1214875764@qq.com'
passwd='jkxfhjonzgwcfihi'    #授权码
to_addr='mjt1220@126.com'
smtp_server='smtp.qq.com'


msg=MIMEText('hello,this is a python test email','plain','utf-8')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自smtp的问候.....','utf-8').encode()

# server=smtplib.SMTP(smtp_server,25)
server=smtplib.SMTP(smtp_server,587)#腾讯
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
