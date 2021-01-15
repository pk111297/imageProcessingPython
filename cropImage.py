import sys
import numpy
import imageio
matA=imageio.imread(sys.argv[1])
height,width,g=matA.shape
newWidth=int(sys.argv[2])
newHeight=int(sys.argv[3])
X=int(sys.argv[4])
X1=X
Y=int(sys.argv[5])
Y1=Y
if height<=Y1+newHeight: newHeight=height-Y1
if width<=X1+newWidth: newWidth=width-X1
matB=numpy.zeros((newHeight,newWidth,g))
r=0
while Y<newHeight+Y1:
 c=0
 X=X1
 while X<newWidth+X1:
  matB[r][c][0]=matA[Y][X][0]
  matB[r][c][1]=matA[Y][X][1]
  matB[r][c][2]=matA[Y][X][2]
  X=X+1
  c=c+1
 r=r+1
 Y=Y+1
imgName=sys.argv[1]
index=imgName.index('.')
imgName=imgName[0:index]+"_crop"+imgName[index:]
imageio.imsave(imgName,matB)	
