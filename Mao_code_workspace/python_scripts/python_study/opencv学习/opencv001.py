# coding=utf-8
# coding=utf-8
import cv2 as cv
import numpy as np


def get_image_info(image):
    """图片信息"""
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def video_demo():
    """打开视频"""
    capture = cv.VideoCapture(0)  # 打开0第一个摄像头
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # 视频进行镜像,左右互换
        cv.imshow("video", frame)
        c = cv.waitKey(2)  # 延迟显示
        if c == 27:
            break


src = cv.imread(r"D:/picture/kantingq/p2254842152.jpg")

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

get_image_info(src)
video_demo()
gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
cv.imwrite("d:/gray.jpg", gray)


cv.waitKey(0)
cv.destroyAllWindows()
