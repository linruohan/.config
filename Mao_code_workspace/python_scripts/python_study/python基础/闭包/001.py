# coding=utf-8




flist = []

for i in range(3):
    print('i=', i)


    def func(x, p=i):
        return x * p


    # def func(x):
    #     return x * i



    print(func)
    flist.append(func)

for f in flist:
    print(f(2))
