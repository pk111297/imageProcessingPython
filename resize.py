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
 r=0
 while r<nh:
  c=0
  while c<nw:
   x=ratio*r
   y=ratio*c
   roundx=int(x)
   roundy=int(y)
   x_diff=abs(roundx-x)
   y_diff=abs(roundy-y)
   r1=image[roundx][roundy][0]
   r2=image[roundx if roundx>=h-1 else roundx+1][roundy][0] 
   r3=image[roundx][roundy if roundy>=w-1 else roundy+1][0]
   r4=image[roundx if roundx>=h-1 else roundx+1][roundy if roundy>=w-1 else roundy+1][0] 
   resize[r][c][0]=fsum((r1*(1-x_diff)*(1-y_diff),r2*x_diff*(1-y_diff),r3*(1-x_diff)*y_diff,r4*x_diff*y_diff))
   g1=image[roundx][roundy][1]
   g2=image[roundx if roundx>=h-1 else roundx+1][roundy][1] 
   g3=image[roundx][roundy if roundy>=w-1 else roundy+1][1]
   g4=image[roundx if roundx>=h-1 else roundx+1][roundy if roundy>=w-1 else roundy+1][1]
   resize[r][c][1]=fsum((g1*(1-x_diff)*(1-y_diff),g2*x_diff*(1-y_diff),g3*(1-x_diff)*y_diff,g4*x_diff*y_diff))
   b1=image[roundx][roundy][2]
   b2=image[roundx if roundx>=h-1 else roundx+1][roundy][2] 
   b3=image[roundx][roundy if roundy>=w-1 else roundy+1][2]
   b4=image[roundx if roundx>=h-1 else roundx+1][roundy if roundy>=w-1 else roundy+1][2]
   resize[r][c][2]=fsum((b1*(1-x_diff)*(1-y_diff),b2*x_diff*(1-y_diff),b3*(1-x_diff)*y_diff,b4*x_diff*y_diff))
   c+=1
  r+=1
 return resize
def main():
 image=imageio.imread(sys.argv[1])
 resize=resizeImage(image,int(sys.argv[2]))
 if(sys.argv[1].find(".jpg")==-1):
  index=sys.argv[1].find(".png")
 else:
  index=sys.argv[1].find(".jpg")
 imgName=sys.argv[1]
 imageio.imsave(imgName[0:index]+"resize"+imgName[index:],resize)
main()
