from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr='**@163.com'
password='授权码'
to_addr='**@163.com'
smtp_server='smtp.163.com'

msg=MIMEMultipart()
msg['From']=_format_addr('许<%s>'%from_addr)
msg['to']=_format_addr('阳<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候','utf-8').encode()
msg.attach(MIMEText('发送带附件的邮件1','plain','utf-8'))
with open('C:\Users\许\Desktop\py\chulihou1.jpg','rb') as f:
    mime=MIMEBase('image','jpg',filename='chulihou1.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='chulihou1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
server=smtplib.SMTP_ssl(smtp_server,465)
server.starttls()
server.set_debuglevel(1)
server.helo(smtp_server)
server.ehlo(smtp_server)
server.login(from_addr,password)
server.send(from_addr,[to_addr],msg.as_string())
server.quit()
print('发送完毕')
