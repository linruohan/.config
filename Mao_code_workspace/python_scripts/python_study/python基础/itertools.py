import itertools
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = [j for i in a for j in i]
# print(b)
#
#
# s=[]
# for i in a:
#     for j in i:
#         s.append(j)
# print(s)
# print(len(a))
# print(len(a))
n=100
for i in itertools.takewhile(lambda x:x<=2*n-1,itertools.count(1,2)):

    print(i)
