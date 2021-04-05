#-*-coding:utf-8-*-
from email.mime.text import MIMEText
import smtplib

mailto_list=["mjt1220@126.com","mmjt1220@163.com"]
#==========================================
# 设置服务器，用户名、口令以及邮箱的后缀
#==========================================
mail_host="smtp.qq.com"
mail_user="1214875764"
mail_pass="pvjgcfbiywxxbaeb"#qq授权码
mail_postfix="qq.com"

def send_mail(to_list,sub,content):
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com:465')
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        return True
    except Exception as e:
        print( str(e))
        return False
    finally:
            s.close()
if __name__ == '__main__':

    if send_mail(mailto_list,"here is subject","here is content"):
        print ("发送成功")
    else:
        print ("发送失败")
