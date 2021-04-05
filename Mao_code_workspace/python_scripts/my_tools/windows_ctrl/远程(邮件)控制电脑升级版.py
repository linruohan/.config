import urllib.request as request
import http.cookiejar as cookiejar
import urllib.parse
import re
import smtplib
from email.mime.text import MIMEText
import time
import win32com.client
import win32con
import win32api
import os
cj = cookiejar.LWPCookieJar()
cookiesupport = request.HTTPCookieProcessor(cj)
opener = request.build_opener(cookiesupport, request.HTTPHandler)
request.install_opener(opener)
speak = win32com.client.Dispatch('SAPI.SPVOICE')


def Login(username, pwd):
    post_url = 'https://mail.163.com/entry/cgi/ntesdoor?df=mail163_letter&from=web&funcid=loginone&iframe=1&language=-1&passtype=1&product=mail163&net=c&style=-1&race=254_292_276_bj&uid=' + username + "@163.com"
    headers = {
        'Host': 'mail.163.com',
        'Origin': 'http://mail.163.com',
        'Referer': 'http://mail.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.39 Safari/537.36'
    }
    post_data = {'savelogin': '0',
                 'url2': 'http://mail.163.com/errorpage/error163.htm',
                 'username': username,
                 'password': pwd
                 }
    post_data = urllib.parse.urlencode(post_data).encode('gbk')
    req = request.Request(post_url, post_data, headers=headers)
    page = request.urlopen(req, timeout=20).read().decode('gb2312')
    sid = re.compile(r'sid=(.+?)&df').findall(page)[0]
    return sid


def check_email():
    mail_url = 'http://mail.163.com/js6/s?sid=' + \
        Login('******', '******') + \
        '&func=mbox:listMessages&LeftNavRecieveMailClick=1&error=no%20Conext.module&mbox_folder_enter=1'
    mail_data = {
        'var': '<?xml version="1.0"?><object><array name="items"><object><string name="func">mbox:getAllFolders</string><object name="var"><boolean name="stats">true</boolean><boolean name="threads">false</boolean></object></object><object><string name="func">mbox:getFolderStats</string><object name="var"><array name="ids"><string>1,3,18</string></array><boolean name="messages">true</boolean><boolean name="threads">false</boolean></object></object><object><string name="func">mbox:listTags</string><object name="var"><boolean name="stats">true</boolean><boolean name="threads">false</boolean></object></object><object><string name="func">mbox:statMessages</string><object name="var"><array name="fids"><int>1</int><int>2</int><int>3</int><int>4</int><int>18</int><int>5</int></array><object name="filter"><string name="defer">19700101:</string></object></object></object><object><string name="func">mbox:statMessages</string><object name="var"><array name="fids"><int>1</int><int>2</int><int>3</int><int>4</int><int>18</int><int>5</int></array><object name="filter"><string name="defer">:20150617</string></object></object></object></array></object>'
    }
    mail_data = urllib.parse.urlencode(mail_data).encode('utf-8')
    req = request.Request(mail_url, mail_data)
    page = request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')
    subject = re.compile(
        r'<string name="subject">(.+?)</string>').findall(page)
    return (subject[len(subject)-1])


def send_email():
    user = '******@163.com'
    pwd = '*******'
    to = ['*****@163.com', '*****@139.com']
    msg = MIMEText('')
    msg['Subject'] = 'OK'
    msg['From'] = user
    msg['To'] = ','.join(to)
    s = smtplib.SMTP('smtp.163.com')
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()


if __name__ == '__main__':
    while True:
        try:
            cmd = check_email()
            command1 = {'关机': 'shutdown -s -t 1',
                        '重启': 'shutdown -r',
                        '关闭浏览器': 'taskkill /F /IM chrome.exe',
                        '关闭QQ': 'taskkill /F /IM QQ.exe',
                        '关闭qq': 'taskkill /F /IM QQ.exe',
                        '关闭wifi': 'taskkill /F /IM kwifi.exe',
                        '关闭音乐': 'taskkill /F /IM cloudmusic.exe',
                        '打开音乐': 'D:\\网易云音乐\\CloudMusic\\cloudmusic.exe',
                        '打开摄像头': 'D:\\Python源码\\摄像头监控.py',
                        '打开监控': 'D:\\Python源码\\winSpyon.py',
                        '打开QQ': 'D:\\腾讯QQ\\Bin\\QQ.exe',
                        '打开qq': 'D:\\腾讯QQ\\Bin\\QQ.exe',
                        '打开wifi': 'D:\\Chrome\\kwifi\\kwifi.exe',
                        '打开ss': 'D:\\代理服务器\\Shadowsocks-win-dotnet4.0-2.3\\Shadowsocks.exe'
                        }
            if cmd in command1.keys():
                speak.Speak('计算机即将' + cmd)
                send_email()
                if cmd.find('打开') == 0:
                    win32api.ShellExecute(0, 'open', command1[cmd], '', '', 1)
                    if cmd == '打开音乐':
                        time.sleep(35)
                        win32api.keybd_event(17, 0, 0, 0)
                        win32api.keybd_event(18, 0, 0, 0)
                        win32api.keybd_event(32, 0, 0, 0)
                        win32api.keybd_event(
                            32, 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(
                            18, 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(
                            17, 0, win32con.KEYEVENTF_KEYUP, 0)
                else:
                    os.system(command1[cmd])
                speak.Speak('计算机已经' + cmd + ',任务执行完毕!')
            time.sleep(60)
        except:
            time.sleep(120)
