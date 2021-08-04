# openCV 인터페이스 기초 / 사용자 인터페이스 및 I/O 처리 

### 윈도우 제어 
- 영상처리는 무엇이라 생각하는가? 영상처리를 한다미로 말하면 2차원 행렬에 대한 연산이라고 할 수 있다 
- OpenCV 에서는 원도우 (window, 창)가 활성화된 상태에서만 마우스나 키보드 이벤트를 감지 할 수 있다. 따라서 이런 이벤트를 감지 해서 처리하려면 원도우를 생성하고 제어할 수 있어야 한다 

- cv2.namedWindow() : 원도우 이름을 설정한 후, 해당 이름으로 원도우 생성
    - namedWindow(winname[,flags])

- cv2.imshow() : 원도우 이름의 mat 행렬을 영상으로 표시함 
    - imshow(winname, mat)

- cv2.destroyAllWindows() : 인수로 지정된 타이들 원도우 파괴

- cv2.moveWindow() : winname 이름의 원도우를 지정된 위치인 (x,y)로 이동, (기존위치는 좌측 상단 )
    - moveWindow(winname, x, y)
 
- cv2.resizeWindow() : 윈도우 크기 재조정 
    - resizeWindow(winname, width, height)
    
### 이벤트 처리 함수 
- 일반적으로 이벤트를 처리하기 위해 콜백(Callback) 함수를 사용한다 
- openCV 에서 대표적으로 키보드 이벤트, 마우스 이벤트, 트랙바(trackbar) 이벤트를 처리하는 콜백 함수들이 있다 

###### 키보드 이벤트 제어 
- cv2.waitKey() : delay : ms(milisscond) 시간 만큼 키 입력을 대기 하고, 키 이벤트가 발생하면 해당 키 값 반환
    - waitKey([,delay])
    - delay <= 0 : 키이벤트 발생까지 무한대기, delay < 0 : 지연시간 동안 키 입력 대기, 지연시간 안에 키 이벤트 없으면 -1 반환 
 
- cv2.waitKeyEX() : waitKey() 와 동일하지만, 전체 키 코드(full key code)를 반환, 화살표 키 등을 입력 받을 때 사용 
    - waitKeyEX([,delay])
    
       