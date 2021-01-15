import numpy
from math import *
import sys
import scipy
import math
import imageio
def eval(value):
  if value>=255:
    return 255
  else:
    if value<=0:
      return 0
    else:
      return value
def gaussian_kernel(size, sigma=1.4):
    x, y = numpy.mgrid[-size:size+1, -size:size+1] #2 for 5x5 matrix
    #print(x,y)
    normal=1/(2.0*numpy.pi*sigma**2)
    g=numpy.exp(-((x**2+y**2)/ (2.0*sigma**2)))*normal
    return g

t=sys.argv[1]
matA=imageio.imread(t)
h,w,g=matA.shape
matB=numpy.zeros((h,w))
#Converting a image to grayscale
r=0
while r<h:
 c=0
 while c<w:
  matB[r][c]=fsum([matA[r][c][0],matA[r][c][1],matA[r][c][2]])/3
  c=c+1
 r=r+1
#converting grayscale to gaussian image blur
gaussian=gaussian_kernel(2) #2 for 5x5 matrix
#print(gaussian)
matC=numpy.zeros((h,w))
gaussianX=int(5/2)
gaussianY=int(5/2)
for r in range(h):
 for c in range(w):
  for row in range(-2,3,1):
   for col in range(-2,3,1):
    if r+row>=0 and c+col>=0 and r+2<h and c+2<w:
     matC[r][c]=eval(matB[r][c]+gaussian[row+1][col+1]*matB[r+row][c+col]) 
#imageio.imsave("SHARP1111.jpg",matC)
#Sobel filtering step
sobel_x = [[-1,0,1],
           [-2,0,2],
           [-1,0,1]]
sobel_y = [[-1,-2,-1],
           [0,0,0],
           [1,2,1]]
gradx=numpy.zeros((h,w))
grady=numpy.zeros((h,w))
sobeloutmag=numpy.zeros((h,w))
sobeloutdir=numpy.zeros((h,w))
print(w-1,h-1)
for y in range(1, w-1):
    for x in range(1, h-1):
        px = (sobel_x[0][0] * matC[x-1][y-1]) + (sobel_x[0][1] * matC[x][y-1])+(sobel_x[0][2] * matC[x+1][y-1]) + (sobel_x[1][0] * matC[x-1][y]) +(sobel_x[1][1] * matC[x][y]) + (sobel_x[1][2] * matC[x+1][y]) + (sobel_x[2][0] * matC[x-1][y+1]) + (sobel_x[2][1] * matC[x][y+1]) + (sobel_x[2][2] * matC[x+1][y+1])
        py = (sobel_y[0][0] * matC[x-1][y-1]) + (sobel_y[0][1] * matC[x][y-1]) +(sobel_y[0][2] * matC[x+1][y-1]) + (sobel_y[1][0] * matC[x-1][y]) +(sobel_y[1][1] * matC[x][y]) + (sobel_y[1][2] * matC[x+1][y]) +(sobel_y[2][0] * matC[x-1][y+1]) + (sobel_y[2][1] * matC[x][y+1]) + (sobel_y[2][2] * matC[x+1][y+1])
        gradx[x][y] = px
        grady[x][y] = py
        sobeloutmag[x][y]=math.sqrt(px*px+py*py)
        sobeloutdir[x][y]=math.atan2(py,px)        
#imageio.imsave("SHARP1112.jpg",sobeloutmag)
for y in range(w):
    for x in range(h):
        if (sobeloutdir[x][y]<22.5 and sobeloutdir[x][y]>=0) or (sobeloutdir[x][y]>=157.5 and sobeloutdir[x][y]<202.5) or (sobeloutdir[x][y]>=337.5 and sobeloutdir[x][y]<=360):
            sobeloutdir[x][y]=0
        elif (sobeloutdir[x][y]>=22.5 and sobeloutdir[x][y]<67.5) or (sobeloutdir[x][y]>=202.5 and sobeloutdir[x][y]<247.5):
            sobeloutdir[x][y]=45
        elif (sobeloutdir[x][y]>=67.5 and sobeloutdir[x][y]<112.5)or (sobeloutdir[x][y]>=247.5 and sobeloutdir[x][y]<292.5):
            sobeloutdir[x][y]=90
        else:
            sobeloutdir[x][y]=135
#Non maximum supression
#imageio.imsave("SHARP1113.jpg",sobeloutmag)
for y in range(1, w-1):
    for x in range(1, h-1):
        if sobeloutdir[x][y]==0:
            if (sobeloutmag[x][y]<=sobeloutmag[x][y+1]) or (sobeloutmag[x][y]<=sobeloutmag[x][y-1]):
                sobeloutmag[x][y]=0
        elif sobeloutdir[x][y]==45:
            if (sobeloutmag[x][y]<=sobeloutmag[x-1][y+1]) or (sobeloutmag[x][y]<=sobeloutmag[x+1][y-1]):
                sobeloutmag[x][y]=0
        elif sobeloutdir[x][y]==90:
            if (sobeloutmag[x][y]<=sobeloutmag[x+1][y]) or (sobeloutmag[x][y]<=sobeloutmag[x-1][y]):
                sobeloutmag[x][y]=0
        else:
            if (sobeloutmag[x][y]<=sobeloutmag[x+1][y+1]) or (sobeloutmag[x][y]<=sobeloutmag[x-1][y-1]):
                sobeloutmag[x][y]=0
#imageio.imsave("SHARP1114.jpg",sobeloutmag)
#DOUBLE THRESHOLDING
m = numpy.max(sobeloutmag)
highThresholdRatio=0.09 #high Threshold
lowThresholdRatio=0.05 #low threshold
highThreshold=m*highThresholdRatio;
lowThreshold=highThreshold*lowThresholdRatio;
res=numpy.zeros((h,w))
weak=numpy.int32(25)
strong=numpy.int32(255)
strong_i,strong_j=numpy.where(sobeloutmag>=highThreshold)
zeros_i,zeros_j=numpy.where(sobeloutmag<lowThreshold)
weak_i,weak_j=numpy.where((sobeloutmag<=highThreshold)&(sobeloutmag>=lowThreshold))
res[strong_i,strong_j]=strong
res[weak_i,weak_j]=weak
#imageio.imsave("SHARP1115.jpg",res)
#Edge Tracking by Hysteresis
for j in range(1, w-1):
 for i in range(1, h-1):
  if (res[i,j] == weak):
   try:
    if ((res[i+1, j-1] == strong) or (res[i+1, j] == strong) or (res[i+1, j+1]== strong) or (res[i, j-1] == strong) or (res[i, j+1] == strong) or (res[i-1, j-1]== strong) or (res[i-1, j] == strong) or (res[i-1, j+1] == strong)):
     res[i,j]=strong
    else:
     res[i,j]=0
   except IndexError as e:
    pass
imageio.imsave("EdgeD.jpg",res)

