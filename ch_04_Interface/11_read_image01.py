import cv2
from matplotlib import pyplot as plt

def print_matInfo( image ):
    if image.dtype == 'uint8':     mat_type = "CV_8U"
    elif image.dtype == 'int8':    mat_type = "CV_8S"
    elif image.dtype == 'uint16':  mat_type = "CV_16U"
    elif image.dtype == 'int16':   mat_type = "CV_16S"
    elif image.dtype == 'float32': mat_type = "CV_32F"
    elif image.dtype == 'float64': mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    ## depth, channel 출력
    print("depth(%s), channels(%s) -> mat_type(%sC%d)"
          % ( image.dtype, nchannel, mat_type,  nchannel))

# 현재 소스 파일의 폴더 경로
from pathlib import Path
source_dir = Path( __file__ ).resolve().parent

# 영상 파일 적재
gray2gray  = cv2.imread( source_dir.joinpath( "./img/read_gray.jpg" ), cv2.IMREAD_GRAYSCALE) 
gray2color = cv2.imread( source_dir.joinpath( "./img/read_gray.jpg" ), cv2.IMREAD_COLOR)

print_matInfo( gray2gray )
print_matInfo( gray2color )

plt.imshow( gray2color )
plt.show()