def eval(value):
  if value>=255:
    return 255
  else:
    if value<=0:
      return 0
    else:
      return value
import sys
import imageio
import numpy
matA=imageio.imread(sys.argv[1]);
#print(matA[0][0][3])
Kmap=numpy.zeros((3,3));
Kmap[0][0]=0
Kmap[0][1]=-1
Kmap[0][2]=0
Kmap[1][0]=-1
Kmap[1][1]=5
Kmap[1][2]=-1
Kmap[2][0]=0
Kmap[2][1]=-1
Kmap[2][2]=0
h,w,g=matA.shape
matB=numpy.zeros((h,w,g));
for r in range(h):
 for c in range(w):
  for row in range(-1,2,1):
   for col in range(-1,2,1):
    if r+row>=0 and c+col>=0 and r+1<h and c+1<w:
     matB[r][c][0]=eval(matB[r][c][0]+Kmap[row+1][col+1]*matA[r+row][c+col][0]) 
     matB[r][c][1]=eval(matB[r][c][1]+Kmap[row+1][col+1]*matA[r+row][c+col][1])
     matB[r][c][2]=eval(matB[r][c][2]+Kmap[row+1][col+1]*matA[r+row][c+col][2])
img=sys.argv[1];
index=img.find(".")
imageio.imsave(img[0:index]+"Sharp"+img[img.rindex('.'):],matB)

