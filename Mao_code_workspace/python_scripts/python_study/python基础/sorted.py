#coding=utf-8



L=[("nad",12),("ndsad",122),("nfdd",33),("grnad",2),("fdnad",32),("ghfdddnad",66),]

# name
def by_sorted(t):
    return -t[-1]
# age:
def by_name(t):
    return t[1]


L1 = sorted(L, key=by_name)
print(L1)


L2 = sorted(L, key=by_sorted)
print(L2)
