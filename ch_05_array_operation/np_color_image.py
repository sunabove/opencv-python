import cv2, numpy as np

h = 100; w = 200 ; shape = (100, 200) 
blue = np.empty( shape )

# cross line
blue[ 50 ] = 255
blue[ :, 100 ] = 255
green = np.empty( shape )
red = np.empty( shape )
image = np.stack( (blue, green, red), axis=2 )

cv2.imshow('Color image', image )
cv2.waitKey(0)

