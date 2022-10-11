'''

    그래프에 임의의 text 값 입력
    - plt.text(x,y, mesg)

    라인 긋기
    -plt.axhline() - 가로로 선 긋기
    -plt.axvline() - 세로로 선 긋기
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(3)
values = [100,200,300]

# 라인 긋기
plt.axhline(150, color='red', linestyle='--')

for idx, v in enumerate(values):
    plt.text(x[idx],v,v)
plt.bar(x,values)

plt.show()
