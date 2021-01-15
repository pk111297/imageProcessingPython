import numpy
from  math import *
import sys
import imageio
t=sys.argv[1]
matA=imageio.imread(t)
h,w,g=matA.shape
matB=numpy.zeros((h,w))
r=0
while r<h:
 c=0
 while c<w:
  matB[r][c]=min(matA[r][c][0],matA[r][c][1],matA[r][c][2])
  c=c+1
 r=r+1
imageio.imsave("MinCaseGray"+sys.argv[1][sys.argv[1].rindex('.'):],matB)
print("Done Using MINCASE Algorithm")
