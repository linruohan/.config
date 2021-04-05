class ListMetaclass(type):
    """这个metaclass可以给我们自定义的MyList增加一个add方法：
    定义ListMetaclass，按照默认习惯，metaclass的类名总是
    以Metaclass结尾，以便清楚地表示这是一个metaclass："""
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    """有了ListMetaclass，我们在定义类的时候
    还要指示使用ListMetaclass来定制类，
    传入关键字参数metaclass"""
    pass

L=MyList()
L.add(1)
print(L)


L2=list()
L2.add(2)
print()
