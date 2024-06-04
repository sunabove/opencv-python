# 11_read_image_01.py
import cv2
from matplotlib import pyplot as plt

# 현재 소스 파일의 폴더 경로
from pathlib import Path
dir = Path( __file__ ).resolve().parent

# 컬러 영상으로 읽음.
image = cv2.imread( dir.joinpath( "./img/read_color.jpg" ), cv2.IMREAD_COLOR)

plt.imshow( image )
plt.show()