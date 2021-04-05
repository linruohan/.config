# coding=utf-8
import cv2 as cv
import numpy as np


def access_pixels(image):
    """像素取反"""
    # print(image.shape)
    # height = image.shape[0]
    # width = image.shape[1]
    # channels = image.shape[2]
    # print("height:%s\n" % height)
    # print("width:%s\n" % width)
    # print("channels:%s\n" % channels)
    # for row in range(height):
    #     for col in range(width):
    #         for c in range(channels):
    #             pv = image[row, col, c]
    #             image[row, col, c] = 255-pv
    image=255-image
    cv.imshow("name", image)

def inverse(image):
    """像素取反  加快效率"""
    dst=cv.bitwise_not(image)
    cv.imshow("inverse image",dst)
    

def create_image():
    img = np.zeros([400, 400, 3], np.uint8)  # 三维的黑色图片
    # 单通道设置
    # img[:,:,0]=np.ones([400,400])*255#blue
    # img[:,:,1]=np.ones([400,400])*255#green
    # img[:,:,2]=np.ones([400,400])*255#red
    # 多通道设置
    img = np.ones([400, 400, ], np.uint8)*127  # 三维的灰色图片

    m1 = np.ones([3, 3], np.uint8)  # 二维int32/float32/uint8
    # cv.convertFp16(m1)
    m1.fill(3223.123123)

    print(m1)
    m2 = m1.reshape([1, 9])  # 一维
    print(m2)
    cv.imshow("new image", img)
    m3=np.array([[1,2,3],[4,5,6],[7,4,32]],np.int32)
    print(m3)

def costs_time(src):
    t1 = cv.getTickCount()
    access_pixels(src)
    t2 = cv.getTickCount()
    costtime = (t2-t1)/cv.getTickFrequency()
    print("time:%s" % (costtime))  # 单位是秒


if __name__ == '__main__':

    src = cv.imread(r"D:/picture/kantingq/p2254842152.jpg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # ===========  do  ================================
    # costs_time(src)
    # create_image()
    #等差数列
    c=np.linspace(0,4,8,endpoint=True,dtype=np.int)
    c1=c.astype(int)#强制转换为另一个int的array
    c2=c.reshape((2,4))#强制转换为另一个[2,4],数据个数必须相等
    # print(c,c2)
    # 等比数列
    d=np.logspace(1,4,4,base=2,endpoint=True)
    d1=d.astype(int)
    # print(d1[::-1])#步长为-1，意味着反转
    # print(d1[::])
    # 随机数列
    # print(np.random.randint(1,3,size=(3,3)))
    # 方阵
    # print(np.diag([1,2,3]))#生成1，2，3 为对角线的方阵
    a=np.array([0,1,2,3,4,5])
    b=a.reshape(-1,1)#  a+b 返回的是一个 5*5 的矩阵

    # print(a+b)#加法必须是行列相同

    # a1=np.matrix(np.array([[2,3,4],[54,32,12]]))
    # print(a1,a1.T)#表示转置 a.I 表示逆矩阵

    a1=np.mat([3,65])
    a2=np.mat([2,2])
    
    a3=np.multiply(a1,a2)
    print(a3)
    # ===========================================

    cv.waitKey(0)
    cv.destroyAllWindows()
