# coding: utf-8
import numpy as np

rng = np.random.default_rng()

print( rng.integers(0, 10, 3) )
print( rng.integers(0, 10, 3, endpoint=True) )
print( rng.random(3) )
print( rng.standard_normal(3) )
print( rng.uniform(1, 10, 3) )
print( rng.normal(5, 2, 3) )