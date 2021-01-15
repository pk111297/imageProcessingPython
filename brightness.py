def eval(value):
 if value>=255:
  return 255
 else:
  if value<0:
   return 0
  else:
   return value
import sys
import numpy
from math import *
import imageio
#factor should be between -255 to 255
factor=int(sys.argv[2])
matA=imageio.imread(sys.argv[1])
h,w,g=matA.shape
matB=numpy.zeros((h,w,3))
for r in range(0,h,1):
 for c in range(0,w,1):
  matB[r][c][0]=eval(matA[r][c][0]+factor)
  matB[r][c][1]=eval(matA[r][c][1]+factor)
  matB[r][c][2]=eval(matA[r][c][2]+factor)
imgName=sys.argv[1]
index=imgName.index('.') 
imgName=imgName[0:index]+"_bright"+imgName[index:]
imageio.imsave(imgName,matB)

