# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 03:25:59 2019

@author: Vi.Ra.S
"""

import numpy as np
import cv2
import time
print("Here")
import serial

import socket

ser = serial.Serial('/dev/ttyACM0', 9600)

m=0

x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
y7=0
print("Here as well")
ser.isOpen()
k=1
#y = [1,3,1]
while( k < 100):
    k += 1
    b = ser.readline()
    #print(b)
    
   # print(type(b))
    str_rn = b.decode()
    
    #print(str_rn)
    #print(type(str_rn))
    str_ = str_rn.rstrip()
    
    #print(str_)
   # print(type(str_))
    a = str_.split("     ")
    #print(a)
    #print(a)
    g=a[0]
    #print(g)
    g= g.split('\t')
    #print(int(g[0]))

    if(len(g)>12):
        x1 = int(g[0])
        x2 = int(g[1])
        x3 = int(g[2])
	x4 = int(g[3])
	x5 = int(g[4])
	x6 = int(g[5])
	
        y1 = int(g[6])
        y2 = int(g[7])
        y3 = int(g[8])
        y4 = int(g[9])
        y5 = int(g[10])
        y6 = int(g[11])
        y7 = int(g[12])
			
    x1=int(x1/250)
    x2=int(x2/250)
    x3=int(x3/250)
    x4=int(x4/250)
    x5=int(x5/250)
    x6=int(x6/250)
        
    y1=int(y1/250)
    y2=int(y2/250)
    y3=int(y3/250)
    y4=int(y4/250)
    y5=int(y5/250)
    y6=int(y6/250)
    y7=int(y7/250)    
    x=[x1,x2,x3,x4,x5,x6]
    y=[y1,y2,y3,y4,y5,y6,y7]
    print(x,y)
   
    x=np.array(x)
    y=np.array(y)
    x=np.reshape(x,(6,1))
    y=np.reshape(y,(1,7))
    #print(x,y)
    pro=np.dot(x,y)
    #print(pro)
    pro1=(pro>250)*250
    pro2=(pro<=250)*pro    
    pro=pro1+pro2
    #print(pro)

    ig = np.ones((700,600)).astype(np.uint8)

    ig[0:100,0:100]=ig[0:100, 0:100]*pro[0][0]
    ig[0:100,100:200]=ig[0:100,100:200]*pro[1][0]    
    ig[0:100,200:300]=ig[0:100,200:300]*pro[2][0]
    ig[0:100,300:400]=ig[0:100,300:400]*pro[3][0]
    ig[0:100,400:500]=ig[0:100,400:500]*pro[4][0]
    ig[0:100,500:600]=ig[0:100,500:600]*pro[5][0]    
    
    ig[100:200,0:100]=ig[100:200,0:100]*pro[0][1]
    ig[100:200,100:200]=ig[100:200,100:200]*pro[1][1]    
    ig[100:200,200:300]=ig[100:200,200:300]*pro[2][1]
    ig[100:200,300:400]=ig[100:200,300:400]*pro[3][1]
    ig[100:200,400:500]=ig[100:200,400:500]*pro[4][1]
    ig[100:200,500:600]=ig[100:200,500:600]*pro[5][1]
    
    ig[200:300,0:100]=ig[200:300 , 0:100]*pro[0][2]
    ig[200:300,100:200]=ig[200:300,100:200]*pro[1][2]    
    ig[200:300,200:300]=ig[200:300,200:300]*pro[2][2]
    ig[200:300,300:400]=ig[200:300,300:400]*pro[3][2]
    ig[200:300,400:500]=ig[200:300,400:500]*pro[4][2]
    ig[200:300,500:600]=ig[200:300,500:600]*pro[5][2]
    
    ig[300:400,0:100]=ig[300:400,0:100]*pro[0][3]
    ig[300:400,100:200]=ig[300:400,100:200]*pro[1][3]    
    ig[300:400,200:300]=ig[300:400,200:300]*pro[2][3]
    ig[300:400,300:400]=ig[300:400,300:400]*pro[3][3]
    ig[300:400,400:500]=ig[300:400,400:500]*pro[4][3]
    ig[300:400,500:600]=ig[300:400,500:600]*pro[5][3]
    
    ig[400:500,0:100]=ig[400:500 , 0:100]*pro[0][4]
    ig[400:500,100:200]=ig[400:500,100:200]*pro[1][4]    
    ig[400:500,200:300]=ig[400:500,200:300]*pro[2][4]
    ig[400:500,300:400]=ig[400:500,300:400]*pro[3][4]
    ig[400:500,400:500]=ig[400:500,400:500]*pro[4][4]
    ig[400:500,500:600]=ig[400:500,500:600]*pro[5][4]
    
    ig[500:600,0:100]=ig[500:600 , 0:100]*pro[0][5]
    ig[500:600,100:200]=ig[500:600,100:200]*pro[1][5]    
    ig[500:600,200:300]=ig[500:600,200:300]*pro[2][5]
    ig[500:600,300:400]=ig[500:600,300:400]*pro[3][5]
    ig[500:600,400:500]=ig[500:600,400:500]*pro[4][5]
    ig[500:600,500:600]=ig[500:600,500:600]*pro[5][5]
    
    ig[600:700,0:100]=ig[600:700 , 0:100]*pro[0][6]
    ig[600:700,100:200]=ig[600:700,100:200]*pro[1][6]    
    ig[600:700,200:300]=ig[600:700,200:300]*pro[2][6]
    ig[600:700,300:400]=ig[600:700,300:400]*pro[3][6]
    ig[600:700,400:500]=ig[600:700,400:500]*pro[4][6]
    ig[600:700,500:600]=ig[600:700,500:600]*pro[5][6]
    

    cv2.imshow("Image", ig)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

ser.close()    

