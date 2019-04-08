
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.show()

    sys.exit(app.exec_())

import cv2

cv2.waitKey(0)
cv2.destroyAllWindows(0)


import numpy as np
h = np.array((4,-4, -6, 7), np.int64)
print(abs(h))
a = np.array([[1, 5, 5, 2],

              [9, -6, 2, 8],

              [3, 7, -9, 1]])
ave = np.average(a[0,0:2])
print(ave)
print(abs(a))
print(np.max(a))
print(np.argmax(a, axis=1))

b = [a[2, 2] for i in range(0, 3)]
print(b)
c = (1, 2, 3)

d = (1, -2, -3)
print(abs(d[1]))
print(abs(d))
e = c-d
f = a[1,:]*255/3
print(f)
g=4
print(str(g+1))

import cv2

img = cv2.imread('E:/colordetectanalysis/JAI_D50_TC918_220_1.bmp')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img_HSV.shape)
print(img_HSV[100, 100])
#HSV空间中，H表示色彩/色度，取值范围 [0，179]，S表示饱和度，取值范围 [0，255]，V表示亮度，取值范围 [0，255]。但是不同的软件使用值不同
img = cv2.imread('E:/colordetectanalysis/JAI_D50_TC918_220_1.bmp')
img_HSV = cv2.cvtColor(img, cv2.COLORMAP_HSV)
cv2.imshow("colormap", img_HSV)
cv2.waitKey(0)
print(img_HSV.shape)
print(img_HSV[40*5, 40*5])
print(img_HSV[40*6, 40*5])
print(img_HSV[40*7, 40*5])
print(img_HSV[40*8, 40*5])
img = cv2.imread('E:/colordetectanalysis/P4_D50_TC918_220_1.bmp')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img[0,0])
print(img_HSV[0, 0, 1])

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
path = 'C:/Users/t03492/Desktop/江西明冠_20190314/手机拍图/微信图片_20190315151427.jpg'
new = path.decoding('gbk').encoding('utf-8')
img= cv2.imread(r"C:/Users/t03492/Desktop/江西明冠_20190314/手机拍图/微信图片_20190315151427.jpg")
print(img.shape)
cv2.cvtColor(img, cv2.colorla)

print("good")