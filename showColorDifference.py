import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

color_image =np.zeros((1120, 800, 3), np.uint8)
#delta_array = np.zeros((27, 20, 3), dtype=float)
colum = []
for i in range(1,21):
    colum.append(str(i)+'R')
    colum.append(str(i)+'G')
    colum.append(str(i)+'B')
data = pd.read_csv('95.csv', header=None)
data.columns = colum
df = pd.DataFrame(data)
df.iloc[1][0:3]
for i in range(0, 28):
    for j in range(0, 20):
        (b, g, r) = (df.iloc[i, 3*j+2], df.iloc[i, 3*j+1], df.iloc[i, 3*j])
        color_image[40*i:(i+1)*40, 40*j:(j+1)*40] = (b, g, r) 
cv2.imwrite('color_image.bmp', color_image)
img = cv2.imread('color_image.bmp')
for i in range(1, 27):
    for j in range(0, 20):
        (b, g, r) = (df.iloc[i, 3*j+2], df.iloc[i, 3*j+1], df.iloc[i, 3*j])
        (b1, g1, r1) = (df.iloc[i+1, 3*j+2], df.iloc[i+1, 3*j+1], df.iloc[i+1, 3*j])
        delta_bgr = (b1-b, g1-g, r1-r)
        print(delta_bgr, round(delta_bgr[2], 1))
        cv2.putText(img, str(round(delta_bgr[2],1)), (40*j+1, 40*(i+1)+10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(img, str(round(delta_bgr[1],1)), ( 40*j+1, 40*(i+1)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
        cv2.putText(img, str(round(delta_bgr[0],1)), ( 40*j+1, 40*(i+1)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
cv2.imwrite('color_image.bmp', img)
cv2.imshow('color_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#delta_array[1][0] = df.iloc[1][0:3]
#print(delta_array[1][0])