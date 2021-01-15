import numpy
from math import *
import sys
import imageio
t=sys.argv[1]
matA=imageio.imread(t)
#h,w,g=matA.shape
h=matA.shape[0]
w=matA.shape[1]
print("H",h,matA.shape[0],"W",w,matA.shape[1])
matB=numpy.zeros((h,w))
r=0
while r<h:
 c=0
 while c<w:
  #print(type(matA[r][c]))
  #print(isinstance(matA[r][c],imageio.core.util.Array)) 
  matB[r][c]=fsum([matA[r][c][0],matA[r][c][1],matA[r][c][2]])/3
  c=c+1
 r=r+1
imageio.imsave("AvgCaseGray"+sys.argv[1][sys.argv[1].rindex('.'):],matB)
print("Done Using AVERAGE CASE Algorithm")
