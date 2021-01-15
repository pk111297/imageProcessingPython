#Before the latest release of the scipy we can read the image by misc.imread but now we have to read the image by imageio.read and write the image using imageio.write
import numpy
from  math import *
import sys
import imageio
t=sys.argv[1]
print(t)
#matA=misc.imread(t)
matA=imageio.imread(t)
h,w,g=matA.shape
matB=numpy.zeros((h,w))
r=0
while r<h:
 	c=0
 	while c<w:
 		matB[r][c]=max(matA[r][c][0],matA[r][c][1],matA[r][c][2])
 		c=c+1
 	r=r+1
#misc.imsave("MaxCaseGray.jpg",matB)
imageio.imwrite("MaxCaseGray"+sys.argv[1][sys.argv[1].rindex('.'):],matB)
print("Done Using MAXCASE Algorithm")
