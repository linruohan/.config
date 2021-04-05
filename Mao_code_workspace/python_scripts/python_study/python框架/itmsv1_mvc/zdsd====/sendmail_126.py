#coding=utf-8
from  email.mime.text import MIMEText
import smtplib

#发件人列表
to_list=["mmjt1220@163.com"]
#对于大型的邮件服务器，有反垃圾邮件的功能，必须登录后才能发邮件，如126,163
mail_server="smtp.126.com"         # 126的邮件服务器
mail_login_user="mjt1220@126.com"   #必须是真实存在的用户，这里我测试的时候写了自己的126邮箱
mail_passwd="mjt1214875"             #必须是对应上面用户的授权码

def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_login_user+"<"+mail_login_user+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_server)
        s.login(mail_login_user,mail_passwd)
        s.sendmail(me, to_list, msg.as_string())
        return True
    except Exception, e:
        print (str(e))
        return False
    finally:
        s.close()
if __name__ == '__main__':
    if send_mail(to_list,"subject","content"):
        print ("发送成功")
    else:
        print("发送失败！")
