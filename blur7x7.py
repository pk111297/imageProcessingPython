import sys
from math import *
import numpy
import imageio
matA=imageio.imread(sys.argv[1])
Kmap=numpy.asarray([[0.00000067,0.00002292,0.00019117,0.00038771,0.00019117,0.00002292,0.00000067],
		 [0.00002292,0.00078633,0.00655965,0.01330373,0.00655965,0.00078633,0.00002292],
		 [0.00019117,0.00655965,0.05472157,0.11098164,0.05472157,0.00655965,0.00019117],
		 [0.00038771,0.01330373,0.11098164,0.22508352,0.11098164,0.01330373,0.00038771],
		 [0.00019117,0.00655965,0.05472157,0.11098164,0.05472157,0.00655965,0.00019117],
		 [0.00002292,0.00078633,0.00655965,0.01330373,0.00655965,0.00078633,0.00002292],
		 [0.00000067,0.00002292,0.00019117,0.00038771,0.00019117,0.00002292,0.00000067]])
h,w,g=matA.shape
matB=numpy.zeros((h,w,g));
Kc=7
Kr=7
KcenX=int(Kc/2)
KcenY=int(Kr/2)
r=0
while r<h:
	c=0
	#print(r)
	while c<w:
		a=-KcenY
		while a<=KcenY:
			if r+a>=0 and r+a<h:
				b=-KcenX
				while b<=KcenX:
					if c+b>=0 and c+b<w:
						matB[r][c]+=Kmap[KcenY+a][KcenX+b]*matA[r+a][c+b]
					b=b+1
			a=a+1
		c=c+1
	r=r+1
imageio.imsave("blur7x7"+sys.argv[1][sys.argv[1].rindex('.'):],matB)
