import unittest,time,re,sys,io,string
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class Persion():
	def __init__(self):
		print (u'__init__是类的构造函数')
	def grow(self):
		print(u'人是高级动物')
	@staticmethod
	def test():
		print(u'静态方法')
# 见调用静态方法的代码：
if __name__=='__main__':
	persion=Persion()
	print(persion.grow())
	Persion.test()
else:
	print(u'主程序正在运行，请稍等!')
