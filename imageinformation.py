from scipy import misc
import numpy
import sys
matA=misc.imread(sys.argv[1])
h,w,g=matA.shape
print("Height: %d,Width: %d"%(h,w))