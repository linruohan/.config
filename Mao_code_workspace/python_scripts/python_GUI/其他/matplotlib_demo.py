# coding=utf-8
from matplotlib import pyplot as plt

# 主要x 和y的个数要相同，不然会报错
x=[3,5,9,16]
y=[2,5,1,7]

x1 = [2,5,8,9]
y1 = [5,3,2,7]

# 可以设置颜色，g代表green, r代表red，y代表yellow，b代表blue
# linewidth = 5，设置线条粗细
# label 设置线条名称
# plt.plot(x, y,'b',linewidth=5,label='Line One')
# plt.plot(x1, y1,'r',linewidth=8,label='Line Two')

# 绘制散点图用scatter函数
# plt.scatter(x, y ,color='b',label='Line 1ne')
# plt.scatter(x1, y1 ,color='r',label='Line 2wo')

# 绘制柱状图用bar函数
plt.bar(x, y ,color='g',label='Line One')
plt.bar(x1, y1 ,color='r',label='Line Two')

# 给这个图，添加标题和XY轴名称，注意这地方不能输入中文，matplotlib应该
# 对中文支持不好，写中文，会显示乱码，方块字
plt.title('xiaohan test_plot chart name')
plt.xlabel('x  axis')
plt.ylabel('y  axis')
# 显示图例
plt.legend()
# 显示网格
# plt.grid(True,color='k')
plt.show()
