import cv2
import numpy as np

class threshold_self:
    def threshold_image(path,Value):
        img = cv2.imread(path,0)
        ret,thresh = cv2.threshold(img,int(Value),255,cv2.THRESH_BINARY)  #必须要在Value上加int，否则程序崩溃，因为不能确定Value的值的类型
        cv2.imshow('Binary_Image',thresh)