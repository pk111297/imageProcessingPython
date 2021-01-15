def eval(value):
 if value<0:
  return 0
 else:
  if value>255:
   return 255
  else:
   return value
import sys
import imageio
import numpy
from math import *
#will be between 0 to 100
C=(510/100)*int(sys.argv[2])
matA=imageio.imread(sys.argv[1])
h,w,g=matA.shape
factor=int((259*(C+255))/(255*(259-C)))
matB=numpy.zeros((h,w,3))
for r in range(0,h,1):
 for c in range(0,w,1):
  matB[r][c][0]=eval(factor*(matA[r][c][0]-128)+128) 
  matB[r][c][1]=eval(factor*(matA[r][c][1]-128)+128)
  matB[r][c][2]=eval(factor*(matA[r][c][2]-128)+128)
imgName=sys.argv[1]
index=imgName.index('.')
imgName=imgName[0:index]+"_contrast"+imgName[index:]
imageio.imsave(imgName,matB)
