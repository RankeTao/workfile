import numpy as np
import pandas as pd 
import cv2
import os

basepath = 'E:/colordetectanalysis/'
entries = os.listdir(basepath)
for entry in entries:
    if '.bmp' in entry:
        filename = os.path.join(basepath, entry)
        HSV_show_name = entry[:-4]+'_HSV.bmp'
        HSV_show_path = os.path.join(basepath, HSV_show_name)

        img = cv2.imread(filename)
        HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        for i in range(0, 28):
            for j in range(0, 20):
                (H, S, V) = HSV_img[40*i, 40*j]
                cv2.putText(img, str(H), (40*j+1, 40*i+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                cv2.putText(img, str(S), ( 40*j+1, 40*i+25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 255, 0), 1)
                cv2.putText(img, str(V), ( 40*j+1, 40*i+37), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (255, 0, 0), 1)
        cv2.imwrite(HSV_show_path, img)
    else:
        pass

print('Bingo! HSV has shown on image!')