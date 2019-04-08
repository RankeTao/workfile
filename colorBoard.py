import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


delta_array = np.zeros((27, 20, 3), dtype=float)
colum = []
for i in range(1,21):
    colum.append(str(i)+'R')
    colum.append(str(i)+'G')
    colum.append(str(i)+'B')
data = pd.read_csv('95.csv', header=None)
data.columns = colum
df = pd.DataFrame(data)
df.iloc[1][0:3]
delta_array[1][0] = df.iloc[1][0:3]
print(delta_array[1][0])
delta = []
for i in range(0,27):
    for j in range(0, 58, 3): 
        rd = df.iloc[i+1][j] - df.iloc[i][j]
        gd = df.iloc[i+1][j+1] - df.iloc[i][j+1]
        bd = df.iloc[i+1][j+2] - df.iloc[i][j+2]
        print(rd, gd, bd)
        delta_array[i][int(j/3)]=(rd, gd, bd)
print(delta_array)
df_r = pd.DataFrame(delta_array[0:27][0:20][1], columns=[i for i in range(1, 21)], index=df.index)
df_r.plot()
plt.show()
