import numpy as np
import pandas as pd 
import cv2
import os

basepath = 'E:/colordetectanalysis/'
entries = os.listdir(basepath)
for entry in entries:
    if '.csv' in entry:
        filename = os.path.join(basepath, entry)
        csv2image_name = entry[:-4]+'.bmp'
        csv2imagepath = os.path.join(basepath, csv2image_name)
        color_image =np.zeros((1120, 800, 3), np.uint8)
        df = pd.read_csv(filename, header=None)
        for i in range(0, 28):
            for j in range(0, 20):
                (b, g, r) = (df.iloc[i, 3*j+2], df.iloc[i, 3*j+1], df.iloc[i, 3*j])
                color_image[40*i:(i+1)*40, 40*j:(j+1)*40] = (b, g, r) 
        for i in range(1, 27):
            for j in range(0, 20):
                (b, g, r) = (df.iloc[i, 3*j+2], df.iloc[i, 3*j+1], df.iloc[i, 3*j])
                (b1, g1, r1) = (df.iloc[i+1, 3*j+2], df.iloc[i+1, 3*j+1], df.iloc[i+1, 3*j])
                delta_bgr = (b1-b, g1-g, r1-r)
                cv2.putText(color_image, str(round(delta_bgr[2],1)), (40*j+1, 40*(i+1)+10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                cv2.putText(color_image, str(round(delta_bgr[1],1)), ( 40*j+1, 40*(i+1)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
                cv2.putText(color_image, str(round(delta_bgr[0],1)), ( 40*j+1, 40*(i+1)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        cv2.imwrite(csv2imagepath, color_image)
    else:
        pass

print('Bingo! All CSV files have been handled!')
