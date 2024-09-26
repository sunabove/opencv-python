# coding: utf-8
import numpy as np

a = np.array( [ 1., 2., 3. ] )
b = np.zeros(3, int)
c = np.zeros_like(a)

print( a.dtype, a.shape )
print( b.dtype, b.shape )
print( c.dtype, c.shape )
