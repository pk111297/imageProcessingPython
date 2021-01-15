import numpy
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
  matB[r][c]=matA[r][c][0]*0.21+matA[r][c][1]*0.72+matA[r][c][2]*0.07
  c=c+1
 r=r+1
imageio.imsave("LumaBGray"+sys.argv[1][sys.argv[1].rindex('.'):],matB)
print("Done Using LUMA B Algorithm")
