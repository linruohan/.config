'''
动态修改有什么意义？直接在MyList定义中写上add()方法
不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
ORM全称“Object Relational Mapping”，即对象-关系映射，
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。
要编写一个ORM框架，所有的类都只能动态定义，
因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个ORM框架。

编写底层模块的第一步，就是先把调用接口
写出来。比如，使用者如果使用这个ORM框架，
想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
'''

#======================================================
'''ORM 框架'''
#========================================================
# 最复杂的ModelMetaclass了
class ModelMetaclass(type):
    """docstring for ModelMetaclass."""
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' %name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s===>%s' %(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings# 保存属性和列的映射关系
        attrs['__table__']=name # 假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)
# 以及基类Model：
class Model(dict,metaclass=ModelMetaclass):
    """docstring for Model."""
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'Model object has no attribute %s'%key)
    def __setattr__(self,key,value):
        self[key]=value

    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('*')
            args.append(getattr(self,k,None))
        sql='insert into %s(%s) values(%s)' %(self.__table__,','.join(fields),','.join(params))
        print('sql:%s' %sql)
        print('args:%s' %str(args))
class Field(object):
    """docstring for Field."""
    def __init__(self, name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return '<%s:%s>' %(self.__class__.__name__,self.name)

class StringField(Field):
    """docstring for StringField."""
    def __init__(self, name):
        super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
    """docstring for IntegerField."""
    def __init__(self, name):
        super(IntegerField, self).__init__(name,'bigint')
#实例化
class User(Model):
    id=IntegerField('id')
    name=StringField('name')
    email=StringField('email')
    passwd=StringField('passwd')

u=User(id=123344,name='xioahan',email='12123123@qq.com',passwd='123222')
u.save()
