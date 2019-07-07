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
import matplotlib.pyplot as plt
import socket

UDP_IP_ADDRESS ="192.168.43.138"
UDP_PORT_NO = 3333

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))

#ser = serial.Serial('/dev/ttyACM0', 9600)

m=0
imgg_copy = np.zeros((1040, 880)).astype(np.uint8)
#tim_sig = 

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
#ser.isOpen()
k=1
#y = [1,3,1]
while(1):
    imgg = np.zeros((1040, 880)).astype(np.uint8)
    k += 1
    #b = data
    #print(b)
    data,addr =serverSock.recvfrom(1024)
   # print(type(b))
    str_rn = data
    
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
    #print(g)

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
			
    x1=int(x1)
    x2=int(x2)
    x3=int(x3)
    x4=int(x4)
    x5=int(x5)
    x6=int(x6)
        
    y1=int(y1)
    y2=int(y2)
    y3=int(y3)
    y4=int(y4)
    y5=int(y5)
    y6=int(y6)
    y7=int(y7) 
 
    x=[x1,x2,x3,x4,x5,x6]
    y=[y1,y2,y3,y4,y5,y6,y7]
    print(x,y)
    for i in range (0,6):
	if x[i] < 7000:
		x[i] = 0

    for i in range (0,7):
	if y[i] < 7000:
		y[i] = 0
    #print(x,y)
    valx = x[0]
    valy = y[0]
    valxp =x[0]
    valyp =y[0]
    cx = [1,3,5,7,9,11]
    cy = [1,3,5,7,9,11,13]
    maxx = 0
    maxy = 0
    maxx1 = 0
    maxy1 = 0
    

    for i in range (0,6):
    	   if x[i] > maxx :
		valxp = valx
		maxx1 = maxx
		valx = x[i]
		maxx = i;	

    for i in range (0,7):
    	   if y[i] > maxy :
		valyp = valy
		maxy1 = maxy
		valy = y[i]
		maxy = i;
    if((valx - valxp) > 3000 or valx == 0):	#
 	cx[maxx1] = -2

    if((valy - valyp) > 3000 or valy == 0):	# 
	cy[maxy1] = -2  
	
    #print(cx[maxx],cy[maxy],cx[maxx1],cy[maxy1],valx,valy,valxp,valyp)

    if( cx[maxx] != -2 and cx[maxx1] != -2 ) : #
	cx[maxx] = ((cx[maxx] + cx[maxx1]) / 2)

    if( cy[maxy] != -2 and cy[maxy1] != -2 ) : # 
	cy[maxy] = ((cy[maxy] + cy[maxy1])) / 2  

    #print(cx[maxx],cy[maxy])
    #print (x);
    
    x1 = [0,0,0,0,0,0,0,0,0,0,0]
    y1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(x,y)
    x1=np.array(x1)
    y1=np.array(y1)
    x1=np.reshape(x1,(11,1))
    y1=np.reshape(y1,(1,13))
    #print(x1,y1)
    pro=np.dot(x1,y1)
    if(cx[maxx] != -2 and cy[maxy] != -2) :
    	pro[cx[maxx] - 1][cy[maxy] - 1] = 1
    #print(pro)
    
    ig = np.ones((650,550)).astype(np.uint8)
    cvx = cy[maxy]-1
    cvy = cx[maxx]-1
    #print(cvx, cvy)
    if((cvx != -3) and (cvy != -3)):
        px_start = cvx*80
        py_start = cvy*80
        for itr in range(0,80):
            for jtr in range(0,80):
                imgg[px_start+itr, py_start+jtr] = 255
                imgg_copy[px_start+itr, py_start+jtr] = 255

    cv2.imshow("Point", imgg)
    cv2.imshow("Image", imgg_copy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   
#ser.close()
serverSock.close()
'''
scale_percent = 60 # percent of original size
width_ = int(pro.shape[1] * scale_percent)
height_ = int(pro.shape[0] * scale_percent)
dim_ = (width_, height_)
# resize image
resized_ = cv2.resize(pro, dim, interpolation = cv2.INTER_AREA) 
'''

