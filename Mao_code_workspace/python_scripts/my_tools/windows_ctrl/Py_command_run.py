# coding=utf-8
__Author__ = 'xiaohan'
import subprocess, os, time
import win32api, win32com


class Command_Run:
    def do_without_output(self,command):
        ret=-1
        ret=os.system(command)
        if ret == 0:
            self.msgbox("Excued [%s] successfully"%ret,u"命令执行")
        else:self.msgbox("Excued [%s] Failed"%ret,u"命令执行")
    def do_with_output(self, command):
        string = ""
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ret = output.stdout.readlines()
        for i in ret:
            if i.strip():
                string += str(i, encoding='gbk')
        return string
    @staticmethod
    def msgbox(message, title):
        win32api.Beep(6000, 100)  # # Beep(freq, dur) freq代表频率,dur代表持续的时间。
        win32api.MessageBox(0, message, title)
    def operate_application(self, option, it):
        if str(option) == "open":
            win32api.ShellExecute(0, 'open', it, '', '', 1)
        else:
            return None


if __name__ == '__main__':
    s = Command_Run()
    out = str(s.do_with_output("ls -l"))
    s.msgbox(out, 'title')
    path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'data\pic\gray.jpg')
    s.operate_application("open",path)

