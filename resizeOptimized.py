import sys
import imageio
import numpy
from math import *
def resizeImage(image,per):
 h,w,b=image.shape
 nh=int((per/100)*h)
 nw=int((per/100)*w)
 resize=numpy.zeros((nh,nw,3))
 ratio=w/nw
 for r in range(0,nh,1):
  for c in range(0,nw,1):
   x=ratio*r
   y=ratio*c
   roundx=int(x)
   roundy=int(y)
   x_diff=abs(roundx-x)
   y_diff=abs(roundy-y)
   for f in range(0,3,1):
    rgb1=image[roundx][roundy][f]
    rgb2=image[roundx if roundx>=h-1 else roundx+1][roundy][f] 
    rgb3=image[roundx][roundy if roundy>=w-1 else roundy+1][f]
    rgb4=image[roundx if roundx>=h-1 else roundx+1][roundy if roundy>=w-1 else roundy+1][f] 
    resize[r][c][f]=fsum((rgb1*(1-x_diff)*(1-y_diff),rgb2*x_diff*(1-y_diff),rgb3*(1-x_diff)*y_diff,rgb4*x_diff*y_diff))
 return resize
def main():
 image=imageio.imread(sys.argv[1])
 newImage=resizeImage(image,int(sys.argv[2]))
 newImgName=sys.argv[1]
 index=newImgName.index('.')
 newImgName=newImgName[0:index]+"_resizeOptimized"+newImgName[index:]
 imageio.imsave(newImgName,newImage)
main()
