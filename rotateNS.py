import numpy
import sys
import math
import imageio
def rotation(im,angle,cw=True):
 if cw==False:
  angle=360-angle
  #print(angle)
 image=imageio.imread(im)
 h,w,b=image.shape
 H,W=h,w
 angleGreaterThan180=False
 #theta=angle
 if(angle>180):
  angleGreaterThan180=True
  angle-=180
 theta=angle
 if(angle>90):
  theta=angle-90
 nw=abs(int((W*math.cos(math.radians(theta)))+(H*math.sin(math.radians(theta)))))	 
 nh=abs(int((W*math.sin(math.radians(theta)))+(H*math.cos(math.radians(theta)))))
 newImage=numpy.zeros((nh,nw,3))
 midx=int(image.shape[1]/2) 
 midy=int(image.shape[0]/2)
 newMidx=int(newImage.shape[1]/2)
 newMidy=int(newImage.shape[0]/2)
 for x in range(0,newImage.shape[1]):
  for y in range(0,newImage.shape[0]):
   ux=x-newMidx
   uy=y-newMidy
   X=(int((ux*math.cos(math.radians(angle)))-(uy*math.sin(math.radians(angle)))))
   Y=(int((ux*math.sin(math.radians(angle)))+(uy*math.cos(math.radians(angle)))))
   X=X+midx
   Y=Y+midy
   if X>=0 and Y>=0 and X<image.shape[1] and Y<image.shape[0]:
    if angleGreaterThan180==True:
     newImage[y][x]=image[-Y][-X] 	
    else: 
     newImage[y][x]=image[Y][X]
 imageio.imsave("rotate.jpg",newImage)
def main():
 image=sys.argv[1]
 angle=sys.argv[2]
 rotation(image,int(angle))
main()
