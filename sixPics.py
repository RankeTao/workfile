import numpy as np
import pandas as pd 
import cv2
import os
import math

#灰度图显示RGB通道的差值，带符号，delta of line delta显示绝对值的差值，带符号

df_r = pd.read_csv('E:/colordetectanalysis/P4_D50_TC918_220_1.csv', header=None) #reference
df_t = pd.read_csv('E:/colordetectanalysis/P4_HRa_mixedLED_TC918_220_1.csv', header=None) #target
delta_E = cv2.imread("C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_1_dE_onHraImage.bmp")

final_image = np.zeros((1160, 4805, 3), np.uint8)
#根据CSV文档数据生成的张彩色图片（28*40，20*40）
color_re = np.zeros((1120, 800, 3), np.uint8)
color_tr = np.zeros((1120, 800, 3), np.uint8)
show_dld_img = np.zeros((1120, 800, 3), np.uint8)
#灰度对比图片表示两张彩色图片中BGR三通相减之后的绝对值的最大值
delta_gray = np.zeros((1120, 800, 3), np.uint8)
delta_gray_max = np.zeros((1120, 800, 3), np.uint8)
delta_array = np.zeros((28, 20, 3), np.int64)
delta_array_gray = np.zeros((28, 20), np.uint8)
for i in range(0, 28):
    for j in range(0, 20):
        (br, gr, rr) = (df_r.iloc[i, 3*j+2], df_r.iloc[i, 3*j+1], df_r.iloc[i, 3*j])
        (bt, gt, rt) = (df_t.iloc[i, 3*j+2], df_t.iloc[i, 3*j+1], df_t.iloc[i, 3*j])
        color_re[40*i:(i+1)*40, 40*j:(j+1)*40] = (br, gr, rr)
        color_tr[40*i:(i+1)*40, 40*j:(j+1)*40] = (bt, gt, rt)
        show_dld_img[40*i:(i+1)*40, 40*j:(j+1)*40] = (bt, gt, rt)
        delta_array[i, j] = (bt-br, gt-gr, rt-rr)
        #print(delta_array)
        #grey = math.sqrt(abs(delta_array[2])**2 + abs(delta_array[2])**2 + abs(delta_array[2])**2)
        delta_array_gray[i, j] = np.max(abs(delta_array[i, j]))
        #print(delta_array_gray)
        delta_gray[40*i:(i+1)*40, 40*j:(j+1)*40] = [delta_array_gray[i, j] for i in range(0, 3)]
        delta_gray_max[40*i:(i+1)*40, 40*j:(j+1)*40] = [delta_array_gray[i, j] for i in range(0, 3)]

graymax = np.max(delta_array_gray)
#将灰度图片在(0,255)之间归一化并将BGR三通相减之后的绝对值的最大值的通道带符号的显示在图片上，并用相应的颜色显示
for i in range(0, 28):
    for j in range(0, 20):
        delta_gray[40*i:(i+1)*40, 40*j:(j+1)*40] = delta_array_gray[i, j]*255/graymax
        delta_gray_max[40*i:(i+1)*40, 40*j:(j+1)*40] = delta_array_gray[i, j]*255/graymax

        cv2.putText(delta_gray, str(round(delta_array[i, j, 2],2)), (40*j+5, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(delta_gray, str(round(delta_array[i, j, 1],2)), (40*j+5, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(delta_gray, str(round(delta_array[i, j, 0],2)), (40*j+5, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (255, 0, 0), 1)

        if np.argmax(abs(delta_array[i, j])) == 0:
            cv2.putText(delta_gray_max, str(round(delta_array[i, j, 0],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif np.argmax(abs(delta_array[i, j])) == 1:
            cv2.putText(delta_gray_max, str(round(delta_array[i, j, 1],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        elif np.argmax(abs(delta_array[i, j])) == 2:
            cv2.putText(delta_gray_max, str(round(delta_array[i, j, 2],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)



delta_delta_gray = np.zeros((1120, 800, 3), np.uint8)
line_delta_array = np.zeros((26, 20, 3), np.int64)
line_delta_array_gray = np.zeros((26, 20), np.uint8)
for i in range(1, 27):
    for j in range(0, 20):
        #reference line delta
        (br, gr, rr) = (df_r.iloc[i, 3*j+2], df_r.iloc[i, 3*j+1], df_r.iloc[i, 3*j])
        (br1, gr1, rr1) = (df_r.iloc[i+1, 3*j+2], df_r.iloc[i+1, 3*j+1], df_r.iloc[i+1, 3*j])
        delta_bgr_re = (br1-br, gr1-gr, rr1-rr)
        cv2.putText(color_re, str(round(delta_bgr_re[2],1)), (40*j+1, 40*(i+1)+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(color_re, str(round(delta_bgr_re[1],1)), ( 40*j+1, 40*(i+1)+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
        cv2.putText(color_re, str(round(delta_bgr_re[0],1)), ( 40*j+1, 40*(i+1)+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        #target line delta
        (bt, gt, rt) = (df_t.iloc[i, 3*j+2], df_t.iloc[i, 3*j+1], df_t.iloc[i, 3*j])
        (bt1, gt1, rt1) = (df_t.iloc[i+1, 3*j+2], df_t.iloc[i+1, 3*j+1], df_t.iloc[i+1, 3*j])
        delta_bgr_tr = (bt1-bt, gt1-gt, rt1-rt)
        cv2.putText(color_tr, str(round(delta_bgr_tr[2],1)), (40*j+1, 40*(i+1)+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(color_tr, str(round(delta_bgr_tr[1],1)), ( 40*j+1, 40*(i+1)+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
        cv2.putText(color_tr, str(round(delta_bgr_tr[0],1)), ( 40*j+1, 40*(i+1)+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        #delta of line delta of target - reference
        line_delta_array[i-1, j] = (abs(delta_bgr_tr[0])-abs(delta_bgr_re[0]),
                                  abs(delta_bgr_tr[1])-abs(delta_bgr_re[1]),
                                  abs(delta_bgr_tr[2])-abs(delta_bgr_re[2])
                                  )
        line_delta_array_gray[i-1, j] = np.max(abs(line_delta_array[i-1, j]))
        delta_delta_gray[40*(i+1):(i+2)*40, 40*j:(j+1)*40] = [line_delta_array_gray[i-1, j] for i in range(0, 3)]

line_graymax = np.max(line_delta_array_gray)
#将两张图片相邻行差值的差值的绝对值最大值的那个值带符号的显示在灰度图片上，并用相应通道的颜色表示。
for i in range(2, 28):
    for j in range(0, 20):
        delta_delta_gray[40*i:(i+1)*40, 40*j:(j+1)*40] = line_delta_array_gray[i-2, j]*255/line_graymax
        if np.argmax(abs(line_delta_array[i-2, j])) == 0:
            cv2.putText(show_dld_img, str(round(line_delta_array[i-2, j, 0],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (255, 0, 0), 1)
        elif np.argmax(abs(line_delta_array[i-2, j])) == 1:
            cv2.putText(show_dld_img, str(round(line_delta_array[i-2, j, 1],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 255, 0), 1)
        elif np.argmax(abs(line_delta_array[i-2, j])) == 2:
            cv2.putText(show_dld_img, str(round(line_delta_array[i-2, j, 2],2)), (40*j+2, 40*i+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 0, 255), 1)

r_sum_re = 0.0
g_sum_re = 0.0
b_sum_re = 0.0
r_sum_tr = 0.0
g_sum_tr = 0.0
b_sum_tr = 0.0

for j in range(4, 18):
    i = 0

    b_sum_re += color_re[i, 40*j, 0]
    g_sum_re += color_re[i, 40*j, 1]
    r_sum_re += color_re[i, 40*j, 2]

    b_sum_tr += color_tr[i, 40*j, 0]
    g_sum_tr += color_tr[i, 40*j, 1]
    r_sum_tr += color_tr[i, 40*j, 2]

print(b_sum_re,g_sum_re,r_sum_re)
print(b_sum_tr,g_sum_tr,r_sum_tr)


b_ave_re = b_sum_re/14
g_ave_re = g_sum_re/14
r_ave_re = r_sum_re/14
print(b_ave_re,g_ave_re,r_ave_re)
b_ave_tr = b_sum_tr/14
g_ave_tr = g_sum_tr/14
r_ave_tr = r_sum_tr/14
print(b_ave_tr,g_ave_tr,r_ave_tr)
delta_ave = (b_ave_tr - b_ave_re, g_ave_tr - g_ave_re, r_ave_tr - r_ave_re)

print(round(delta_ave[2], 2), round(delta_ave[1], 2), delta_ave[0])

for j in range(4, 18):
    i = 0
    color_re[40*i:(i+1)*40, 40*j:(j+1)*40]
    cv2.putText(color_re, str(color_re[i, 40*j, 2]), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    cv2.putText(color_re, str(color_re[i, 40*j, 1]), (40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    cv2.putText(color_re, str(color_re[i, 40*j, 0]), (40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

    cv2.putText(color_tr, str(color_tr[i, 40*j, 2]), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    cv2.putText(color_tr, str(color_tr[i, 40*j, 1]), (40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    cv2.putText(color_tr, str(color_tr[i, 40*j, 0]), (40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
    
    delta_gray[40*i:(i+1)*40, 40*j:(j+1)*40] = [10, 10, 10]
    cv2.putText(delta_gray, str(round(delta_ave[2], 2)), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    cv2.putText(delta_gray, str(round(delta_ave[1], 2)), (40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    cv2.putText(delta_gray, str(round(delta_ave[0], 2)), (40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)


final_image[0:40, 0:4805] = (200, 0, 0) #添加一行序号
final_image[40:1160, 0:800] = color_re
final_image[40:1160, 800] = (255, 255, 255)
final_image[40:1160, 801:1601] = color_tr
final_image[40:1160, 1601] = (255, 255, 255)
final_image[40:1160, 1602:2402] = delta_gray
final_image[40:1160, 2402] = (255, 255, 255)
final_image[40:1160, 2403:3203] = delta_gray_max
final_image[40:1160, 3203] = (255, 255, 255)
final_image[40:1160, 3204:4004] = show_dld_img
final_image[40:1160, 4004] = (255, 255, 255)
final_image[40:1160, 4005:4805] = delta_E


for picNum in range(0,6): 
    for j in range(0, 20):
        cv2.putText(final_image, str(j+1), (801*picNum+40*j+5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,  (10, 10, 10), 2)

cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/sixPics/P4_D50&HRamixedLED_TC918_220_1.bmp', final_image )
cv2.imshow('compare', final_image)
cv2.waitKey(0)