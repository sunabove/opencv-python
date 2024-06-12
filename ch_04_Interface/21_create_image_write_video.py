# 21_create_image_write_video.py

import cv2
import numpy as np

# 현재 소스 파일의 폴더 경로
from pathlib import Path
dir = Path( __file__ ).resolve().parent

# blue, green, red 채널 영상 생성
size = (height, width) = (256, 255)
b = np.zeros( size, dtype = 'uint8')
g = np.zeros( size, dtype = 'uint8')
r = np.zeros( size, dtype = 'uint8')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc( *"MP4V")
# 비디오 출력 파일 
out = cv2.VideoWriter( dir.joinpath( "img/video_output_02.mp4" ), fourcc, 10, (width, height))

for i in range( width ):
    # 첫 번째 열부터 마지막 ​​열까지 청색의 강도를 점차적으로 높입니다.
    b[ :, i ] = i
    # 첫 번째 행부터 마지막 ​​행까지 녹색의 강도를 점차적으로 감소시킵니다.
    g[ i, : ] = 255 - i
    # 첫 번째 행부터 마지막 ​​행까지 적색의 강도를 0으로 설정합니다.
    r[ :, i ] = 0

    frame = cv2.merge([b, g ,r ] )
    out.write(frame)
pass

out.release() # 출력 파일 자원 해제

print( "동영상 변환 완료" )