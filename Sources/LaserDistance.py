
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:05:11 2020

@author: Firoj
"""

import numpy as np
import re

def utf16_decimals(char):
    char =re.sub('[,+]','',char)
    char =re.sub('[E]','e',char)
    return int(float(char))
file=open(r'F:\MScEE\ATLaser\project\result_F\text_z10.txt', encoding='utf-16-le')
lines=file.readlines()
pxl=np.zeros((512, 512))#creat empty 2D array
lenth = (len(lines))
row = 0
for l in lines[24:lenth]:#first row data print, 23-24 ...
    line=(l.split())
    for i in range(1,513):
        encoded_char = utf16_decimals(line[i])
        pxl[row, i-1] = encoded_char
    row +=1
data = pxl.astype(np.float64) / pxl.max() # normalize 
data = 255 - 255 *data # 'now scale by 255
r1 = 0
c1 = 0
center1 = []
center2 = []
for row in data:
    for col in row:
        v = np.mean(col)
        if(v <= 120):
            #print(col)
            #print("r1:", r1, "c1", c1)
            center1.append(r1)
            center2.append(c1)
        c1+=1
    r1 += 1
    c1 = 0
print(len(center1), len(center2))
xx1 = np.min(center1)
xx2 = np.max(center1)
yy1 = np.min(center2)
yy2 = np.max(center2)
print("row: " ,np.mean([xx1, xx2]))
print("col: " ,np.mean([yy1, yy2]))
#transfer matrix linear
X = (5/512)*np.mean([yy1, yy2]) - 2.5

Y = (-5/512)*np.mean([xx1, xx2]) + 2.5

print("final X and Y in mm: ", X, Y)

#%%Distance Calculation
x1=235; x2=245
u1=-1.1767578125
u2=-0.6103515625 # position of object for calibration, see 5.3 in the Project Report
u= -0.888671875 # object at position z 0
d=x2-x1
k=u2*x2-u1*x1
n=(u1-u2)*x1*x2
x_1=n/(u*d-k)
print("Distance in mm:", x_1) # 
print("Error in mm:", x_1 - 240) # error according theoretical distance 240