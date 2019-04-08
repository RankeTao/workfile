import numpy as np 
import pandas as pd 
import cv2
import math

#显示参数调整
bs = 40 # block size = bs*bs pixels
s_LR = 2 # 文字在block size显示的左右位置
s_UD = 30 ## 文字在block size显示的左右位置
dE_Lthreshlod = 1 # delta_E的阈值，只显示0-dE_threshlod之间的值
dE_Hthreshlod = 10 # delta_E的阈值，只显示0-dE_threshlod之间的值

#读入高显色光源的图片
HRa_img1 = cv2.imread("C:/Users/t03492/Desktop/color_analysis_pictures/colorBlock/JAI_HRa_mixedLED_TC918_220_1.bmp")
HRa_img2 = cv2.imread("C:/Users/t03492/Desktop/color_analysis_pictures/colorBlock/JAI_HRa_mixedLED_TC918_220_2.bmp")
#print(HRa_img2.shape)
HRa_img = np.zeros((55*bs, 20*bs, 3), np.uint8)
HRa_img[0:28*bs, 0:20*bs] = HRa_img1
HRa_img[28*bs:55*bs, 0:20*bs] = HRa_img2[1*bs:28*bs, 0:20*bs]
#pandas读取数据
df = pd.read_excel("C:/Users/t03492/Desktop/TC918@CLJ_data.xlsx")
df1 = pd.read_excel("C:/Users/t03492/Desktop/TC918@ZMF_data.xlsx")


#色差的最终结果将显示在这几张图片中，三种图片的RGB数据都一样来自‘TC918@ZMF_data.xlsx’文件
BGR_IMAGE = np.zeros((55*bs, 20*bs, 3), np.uint8) # CLJ的色差数据显示在这种图片上
BGR1_IMAGE = np.zeros((55*bs, 20*bs, 3), np.uint8) # ZMF的色差数据显示在这种图片上
dE_IMAGE = np.zeros((55*bs, 20*bs, 3), np.uint8) # 两者的数据差别显示在这种图片上
#创建矩阵将文件中的数据写进去
XYZ_array = np.zeros((55, 20, 3), np.float)
Lab_array = np.zeros((55, 20, 3), np.float)


BGR1_array = np.zeros((55, 20, 3), np.uint8)
XYZ1_array = np.zeros((55, 20, 3), np.float)
Lab1_array = np.zeros((55, 20, 3), np.float)

#创建矩阵将色差的计算结果写进去第一行没有数据，全为0
delta_E = np.zeros((55, 20), np.float)
delta_E1 = np.zeros((55, 20), np.float)
dE_array = np.zeros((55, 20), np.float)
#处理数据并写入相应的矩阵中
for i in range(0, 55):
    for j in range(0, 20):
        XYZ_array[i, j] = (df['XYZ_X'][j*55+i], df['XYZ_Y'][j*55+i],df['XYZ_Z'][j*55+i])
        Lab_array[i, j] = (df['LAB_L'][j*55+i], df['LAB_A'][j*55+i],df['LAB_B'][j*55+i])
        
        BGR1_array[i, j] = (df1['RGB_B'][j*55+i], df1['RGB_G'][j*55+i],df1['RGB_R'][j*55+i])
        XYZ1_array[i, j] = (df1['XYZ_X'][j*55+i], df1['XYZ_Y'][j*55+i],df1['XYZ_Z'][j*55+i])
        Lab1_array[i, j] = (df1['LAB_L'][j*55+i], df1['LAB_A'][j*55+i],df1['LAB_B'][j*55+i])
#BGR1_array[2,0]=(22.89, 95.62, 28.99)
#print(BGR1_array[2,0])

#使用‘TC918@ZMF_data.xlsx’文件的RGB数据生成三张一样的图片
for i in range(0, 55):
    for j in range(0, 20):
        BGR_IMAGE[i*bs:(i+1)*bs, j*bs:(j+1)*bs] = BGR1_array[i, j]
        BGR1_IMAGE[i*bs:(i+1)*bs, j*bs:(j+1)*bs] = BGR1_array[i, j]
        dE_IMAGE[i*bs:(i+1)*bs, j*bs:(j+1)*bs] = BGR1_array[i, j]

#计算色差数据并显示
for i in range(0, 54):
    for j in range(0, 20):
        #计算delta_E, 下一行减上一行的色差，显示在下一行
        (L, a, b) = (Lab_array[i, j, 0], Lab_array[i, j, 1], Lab_array[i, j, 2])
        (L_nl, a_nl, b_nl) = (Lab_array[i+1, j, 0], Lab_array[i+1, j, 1], Lab_array[i+1, j, 2])
        delta_E[i+1, j] = math.sqrt((L_nl-L)**2 + (a_nl-a)**2 + (b_nl-b)**2)
        #print(delta_E[i+1, j])
        (L1, a1, b1) = (Lab1_array[i, j, 0], Lab1_array[i, j, 1], Lab1_array[i, j, 2])
        (L1_nl, a1_nl, b1_nl) = (Lab1_array[i+1, j, 0], Lab1_array[i+1, j, 1], Lab1_array[i+1, j, 2])
        delta_E1[i+1, j] = math.sqrt((L1_nl-L1)**2 + (a1_nl-a1)**2 + (b1_nl-b1)**2)
        #ZMF文件计算的色差减去CLJ文件数据计算的色差
        dE_array[i+1, j] = delta_E1[i+1, j] - delta_E[i+1, j]
        #print(delta_E1[i+1, j])
        
        #将色差数据结果有条件的显示在图片上
        if dE_Lthreshlod < delta_E[i+1, j] < dE_Hthreshlod:
            cv2.putText(BGR_IMAGE, str(round(delta_E[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+s_UD), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (10, 10, 10), 1)
        else:
            pass
        
        if dE_Lthreshlod < delta_E1[i+1, j] < dE_Hthreshlod:
            cv2.putText(BGR1_IMAGE, str(round(delta_E1[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+s_UD), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 0, 255), 1)
        else:
            pass
        #将CLJ色差数据结果有条件的显示在HRa_img中
        # if dE_Lthreshlod < delta_E[i+1, j] < dE_Hthreshlod:
        #     cv2.putText(HRa_img, str(round(delta_E[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+s_UD), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (150, 150, 150), 1)
        # else:
        #     pass
        #将ZMF色差数据结果有条件的显示在HRa_img中
        if dE_Lthreshlod < delta_E1[i+1, j] < dE_Hthreshlod:
            cv2.putText(HRa_img, str(round(delta_E1[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+s_UD), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (150, 150, 150), 1)
        else:
            pass
        #将ZMF文件数据计算的色差减去CLJ文件数据计算的色差的最终结果显示dE_IMAGE上
        if j%2 == 0:
            cv2.putText(dE_IMAGE, str(round(dE_array[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 50, 50), 1)
        elif j%2 == 1:
            cv2.putText(dE_IMAGE, str(round(dE_array[i+1, j],2)), (bs*j+s_LR, bs*(i+1)+35), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

# print(XYZ_array[5:10, 7])
# print(Lab_array[5:10, 7])
# print(delta_E[5:10, 7])
#print(delta_E[15:20, 7])
#print(delta_E1[1:5, 6])


# cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_1_BGR_dE.bmp', BGR_IMAGE[0:28*bs, 0:20*bs])
# cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_2_BGR_dE.bmp', BGR_IMAGE[28*bs:55*bs, 0:20*bs])
# cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_1_BGR1_dE.bmp', BGR1_IMAGE[0:28*bs, 0:20*bs])
# cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_2_BGR1_dE.bmp', BGR1_IMAGE[28*bs:55*bs, 0:20*bs])
# cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/ddE_IMAGE.bmp', dE_IMAGE)
cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_1_dE1_onHraImage_JAI.bmp', HRa_img[0:28*bs, 0:20*bs])
cv2.imwrite('C:/Users/t03492/Desktop/color_analysis_pictures/colorBoard_show/TC918_2_dE1_onHraImage_JAI.bmp', HRa_img[28*bs:55*bs, 0:20*bs])


# cv2.imshow('TC918_1_BGR_dE.bmp', BGR_IMAGE[0:28*bs, 0:20*bs])
# cv2.imshow('TC918_2_BGR_dE.bmp', BGR_IMAGE[28*bs:55*bs, 0:20*bs])
# cv2.imshow('TC918_1_BGR1_dE.bmp', BGR1_IMAGE[0:28*bs, 0:20*bs])
# cv2.imshow('TC918_2_BGR1_dE.bmp', BGR1_IMAGE[28*bs:55*bs, 0:20*bs])
# cv2.imshow('ddE_IMAGE.bmp', dE_IMAGE)
cv2.imshow('HRa_img', HRa_img)
cv2.imshow('TC918_1_dE1_onHraImage_JAI.bmp', HRa_img[0:28*bs, 0:20*bs])
cv2.imshow('TC918_2_dE1_onHraImage_JAI.bmp', HRa_img[28*bs:55*bs, 0:20*bs])

cv2.waitKey(0)