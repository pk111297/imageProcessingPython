import sys
from math import *
import numpy
import imageio
matA=imageio.imread(sys.argv[1]);
Kmap=numpy.zeros((3,3));
Kmap[0][0]=0.0625
Kmap[0][1]=0.125
Kmap[0][2]=0.0625
Kmap[1][0]=0.125
Kmap[1][1]=0.25
Kmap[1][2]=0.125
Kmap[2][0]=0.0625
Kmap[2][1]=0.125
Kmap[2][2]=0.0625
h,w,g=matA.shape
matB=numpy.zeros((h,w,g));
Kc=3
Kr=3
KcenX=int(Kc/2)
KcenY=int(Kr/2)
r=0
while r<h:
 c=0
 while c<w:
  matB[r][c]=Kmap[KcenY][KcenX]*matA[r][c] 
  matB[r][c]+=Kmap[KcenY][KcenX+1]*matA[r][c+1] if r+1<h and c+1<w else 0 
  matB[r][c]+=Kmap[KcenY][KcenX-1]*matA[r][c-1] if r-1>=0 and c-1>=0 else 0
  matB[r][c]+=Kmap[KcenY-1][KcenX-1]*matA[r-1][c-1] if r-1>=0 and c-1>=0 else 0
  matB[r][c]+=Kmap[KcenY-1][KcenX]*matA[r-1][c] if r-1>=0 and c-1>=0 else 0
  matB[r][c]+=Kmap[KcenY-1][KcenX+1]*matA[r-1][c+1] if r-1>=0 and c+1<w else 0
  matB[r][c]+=Kmap[KcenY+1][KcenX-1]*matA[r+1][c-1] if r+1<h and c-1>=0 else 0
  matB[r][c]+=Kmap[KcenY+1][KcenX]*matA[r+1][c] if r+1<h and c-1>=0 else 0
  matB[r][c]+=Kmap[KcenY+1][KcenX+1]*matA[r+1][c+1] if r+1<h and c+1<w else 0  
  c=c+1
 r=r+1
imageio.imsave("blur3x3"+sys.argv[1][sys.argv[1].rindex('.'):],matB)

