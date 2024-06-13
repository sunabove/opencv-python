# 24_matplatlib_sub_plot.py

import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 여러 그래프 생성
plt.figure()

# 첫 번째 그래프: 사인 함수
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Sine')

# 두 번째 그래프: 코사인 함수
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Cosine')

# 레이아웃을 조정하여 그림 중첩 방지
plt.tight_layout() 
# 그래프 표시
plt.show()