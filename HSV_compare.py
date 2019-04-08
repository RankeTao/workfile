import numpy as np
import pandas as pd 
import cv2
import os

img1 = cv2.imread('E:/colordetectanalysis/P4_emb_IT87_220.bmp')
HSV_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img2 = cv2.imread('E:/colordetectanalysis/P4_HRa_mixedLED_IT87_220.bmp')
HSV_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

final_image = np.zeros((1160, 2402, 3), np.uint8)
delta_gray = np.zeros((1120, 800, 3), np.uint8)
delta_array = np.zeros((28, 20, 3), np.int64)
delta_array_gray = np.zeros((28, 20), np.uint8)

for i in range(0, 28):
    for j in range(0, 20):
        (H1, S1, V1) = HSV_img1[40*i, 40*j]
        (H2, S2, V2) = HSV_img2[40*i, 40*j]
        cv2.putText(img1, str(H1), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(img1, str(S1), (40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
        cv2.putText(img1, str(V1), (40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        cv2.putText(img2, str(H2), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(img2, str(S2), (40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
        cv2.putText(img2, str(V2), (40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        #用python处理图像时，可能会涉及两幅图像像素值之间的加减运算，这里需要注意的是图像像素值是ubyte类型，
        #ubyte类型数据范围为0~255，若做运算出现负值或超出255，则会抛出异常
        HSV_delta = (int(H2)-int(H1), int(S2)-int(S1), int(V2)-int(V1))
        #print(HSV_delta)
        delta_array[i, j] = HSV_delta
        #print(delta_array[i, j])
        delta_array_gray[i, j] = abs(delta_array[i, j, 1]) #饱和度差值的的绝对值
        #print(delta_array_gray[i, j])
        delta_gray[40*i:40*(i+1), 40*j:40*(j+1)] = [delta_array_gray[i, j] for i in range(0, 3)]

graymax = np.max(delta_array_gray)

for i in range(0, 28):
    for j in range(0, 20):
        delta_gray[40*i:(i+1)*40, 40*j:(j+1)*40] = delta_array_gray[i, j]*255/graymax
        #cv2.putText(delta_gray, str(delta_array[i, j, 0]), (40*j+2, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        if delta_array[i, j, 1] < 0:
            cv2.putText(delta_gray, str(delta_array[i, j, 1]), (40*j+2, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        else:
            cv2.putText(delta_gray, str(delta_array[i, j, 1]), (40*j+2, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(delta_gray, str(delta_array[i, j, 2]), (40*j+2, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

final_image[0:40, 0:2402] = (200, 0, 0) #添加一行序号
final_image[40:1160, 0:800] = img1
final_image[40:1160, 800] = (255, 255, 255)
final_image[40:1160, 801:1601] = img2
final_image[40:1160, 1601] = (255, 255, 255)
final_image[40:1160, 1602:2402] = delta_gray

for picNum in range(0,3): 
    for j in range(0, 20):
        cv2.putText(final_image, str(j+1), (801*picNum+40*j+5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,  (10, 10, 10), 2)

cv2.imwrite('P4_emb&HRamixedLED_IT87_220_HSV.bmp', final_image )
cv2.imshow('compare', final_image)
cv2.waitKey(0)

print('Bingo! HSV has shown on image!')