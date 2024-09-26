# coding: utf-8
import numpy as np

a = np.arange( 1, 6 )

print( a[1] )
print( a[2:4] )
print( a[-2:] )
print( a[::2] )
print( a[ [1, 3, 4] ] )

a[ 2: 4 ] = 0 
print( a )