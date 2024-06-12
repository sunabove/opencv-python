# 20_read_write_video_file.py

import cv2

# 현재 소스 파일의 폴더 경로
from pathlib import Path
dir = Path( __file__ ).resolve().parent

# 정지 영상 읽기
img = cv2.imread( dir.joinpath( "img/video_input_01.png") )
# 정지 영상의 높이, 폭, 채널
height, width, channels = img.shape

cv2.imshow( "image", img)

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc( *"MP4V")
# 비디오 출력 파일 
out = cv2.VideoWriter( dir.joinpath( "img/video_output_01.mp4" ), fourcc, 10, (width, height))

# 채널 분리
(b, g, r) = cv2.split( img )
for i in range(100):
    # blue 채널의 값들을 1씩 증가 시킴
    b = b + 1  
    # 채널 합치기
    frame = cv2.merge([b, g ,r ] )
    # 비디오 프레임 쓰기
    out.write(frame)
pass

out.release() # 비디오 쓰기 파일 해제
cv2.waitKey( 0 )  # 키 입력 무한 대기