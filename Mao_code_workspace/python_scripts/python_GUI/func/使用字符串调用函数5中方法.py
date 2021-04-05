# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'


def chinese(text):
    print("chinese", text)


def english(text):
    print("english", text)


func = 'chinese'
# 1
eval(func)("你好eval is evil")
# 2
locals()[func]("你好 locals")
# 3
globals()[func]("你好 globals")


class Foo:
    def chinese(self, text):
        print("chinese", text)

    def english(self, text):
        print("english", text)

    def all(self):
        for i in ['chinese', 'english']:
            getattr(self, i)("你好 FOO")


# 4
foo = Foo()
getattr(foo, 'chinese')("你好 FOO")
foo.all()
# 5
from operator import methodcaller

methodcaller('chinese', "你好 methodcaller")(foo)
