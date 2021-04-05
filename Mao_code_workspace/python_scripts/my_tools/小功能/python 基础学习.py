# coding=utf-8
# a = 5
# b = 10
# # 交换a 和 b
# a, b = b, a
# print(a,b)
#
# bag = [0] * 10
# print(bag)
#
# bag_of_bags = [[0] for _ in range(5)]
# # [[0], [0], [0], [0], [0]]
#
# bag_of_bags[0][0] = 1
# # [[1], [0], [0], [0], [0]]
# print(bag_of_bags)
#
# name = "Raymond"
# age = 22
# born_in = "Oakland, CA"
# string = "Hello my name is {0} and I'm {1} years old. I was born in {2}.".format(name, age, born_in)
# print(string)


# 统计字符出现的次数count
countr = {}
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
print(bag.count(2))
for i in bag:
    countr[i] = countr.get(i, 0) + 1

for i in range(10):
    print("Count of {}: {}".format(i, countr.get(i, 0)))
print(countr)
print(countr.get(8))
s = {value: bag.count(value) for value in bag}
print(s)
print(bag[::-1])  # 翻转

# 前5个
for i in bag[:5]:
    print(i)
print('*' * 10)
# 最后5个
for i in bag[-5:]:
    print(i)

# 隔二取一
for index, value in enumerate(bag[::2]):
    print(index, value)
print(bag[::-1])  # 翻转
