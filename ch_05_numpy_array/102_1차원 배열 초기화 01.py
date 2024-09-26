# coding: utf-8
import numpy as np

# 1차원 배열 초기화
a = np.array( [ 1., 2., 3. ] )
b = np.zeros(3, int)
c = np.zeros_like(a)

# 주요 속성 값 출력
print( a.dtype, a.shape )
print( b.dtype, b.shape )
print( c.dtype, c.shape )
