import cv2
import numpy as np 

img1 =cv2.imread('C:/Users/t03492/Desktop/JAI_D50_TC918_220_1_HSV.bmp')#路径中不能有中文
print(type(img1))
print(img1.shape)
print(img1[3][3])
img2 = np.array(cv2.imread("C:/Users/t03492/Desktop/JAI_D50_TC918_220_2_HSV.bmp"))
img_stitch = np.zeros((1120, 1600, 3), np.uint8)

img_stitch[0:1120, 0:800] = img1
img_stitch[0:1120, 800:1600] = img2

cv2.imwrite('stitchImages.bmp', img_stitch)
cv2.imshow('Result', img_stitch) 
cv2.waitKey(0)
