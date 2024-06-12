# 17_set_camera_atty.py

import cv2

# 그림자 문자 출력
def put_string(frame, text, pt, value=None, color=(120, 200, 90)) :
    text = str(text) + str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2) # 그림자 효과
    cv2.putText(frame, text, pt   , font, 0.7, color, 2) # 작성 문자

# 줌 트랙바 콜백 함수
def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value) # 줌 설정 

# 포커스 트랙바 콜백 함수
def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

capture = cv2.VideoCapture(0)

if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

title = "Change Camera Properties"              # 윈도우 이름 지정
cv2.namedWindow(title)                          # 윈도우 생성 - 반드시 생성 해야함
cv2.createTrackbar("zoom" , title, 0, 10, zoom_bar)
cv2.createTrackbar("focus", title, 0, 40, focus_bar)

while True:
    ret, frame = capture.read()     # 카메라 영상 읽기
    if not ret: break # 영상을 못 읽었을 경우, 루프 해제
    if cv2.waitKey(30) >= 0: # ESC 키 입력시 루프 해제
        break

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))

    put_string(frame, "zoom : " , (10, 240), zoom)   # 줌 값 표시
    put_string(frame, "focus : ", (10, 270), focus)    # 초점 값 표시 

    cv2.imshow(title, frame) # 영상 출력
pass

capture.release() # 비디오 연결 해체