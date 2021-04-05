# coding=utf-8
import pickle
'''pickle模块接口，即序列化和反序列化。
其中【【序列化操作】】包括：
1、pickle.dump()
pickle.dump(obj, file, protocol=None,*,fix_imports=True)
该方法实现的是将序列化后的对象obj以二进制形式写入文件file中，进行保存。
等同于 Pickler(file, protocol).dump(obj)
import picklewith open('svm_model_iris.pkl', 'wb') as f:
    pickle.dump(svm_classifier, f)

2、pickle.dumps()方法的参数如下：
pickle.dumps(obj, protocol=None,*,fix_imports=True)
pickle.dumps()方法跟pickle.dump()方法的区别在于，
pickle.dumps()方法不需要写入文件中，它是直接返回一个序列化的bytes对象

【【反序列化操作】】包括：
3、pickle.load()
pickle.load(file, *,fix_imports=True, encoding=”ASCII”. errors=”strict”)
Unpickler(file).load() 实现的功能跟 pickle.load() 是一样的
该方法实现的是将序列化的对象从文件file中读取出来。

4、pickle.loads(bytes_object, *,fix_imports=True, encoding=”ASCII”. errors=”strict”)
pickle.loads()方法跟pickle.load()方法的区别在于，
pickle.loads()方法是直接从bytes对象中读取序列化的信息，而非从文件中读取。

'''

with open('D:\\atom\\tkinter\\1.txt','wb') as f:
    data={'admin':'admin'}
    pickle.dump(data,f)
with open('D:\\atom\\tkinter\\1.txt','rb') as f:
    s=pickle.load(f)
    print(s)
