# coding=utf-8
import cv2 as cv
import numpy as np

def color_space(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    cv.imshow("gray",gray)
    hsv=cv.cvtColor(image,cv.COLOR_RGB2HSV)
    cv.imshow("hsv",gray)
    yuv=cv.cvtColor(image,cv.COLOR_RGB2YUV)
    cv.imshow("yuv",gray)
    ycrcb=cv.cvtColor(image,cv.COLOR_RGB2YCrCb)
    cv.imshow("ycrcb",gray)
    

if __name__ == '__main__':

    src = cv.imread(r"D:/picture/kantingq/p2254842152.jpg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # ===========  do  ================================
    color_space(src)
    # ===========================================

    cv.waitKey(0)
    cv.destroyAllWindows()
