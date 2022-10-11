'''

    그래프 파일 저장
    fig = plt.figure()

    fig.savefig(파일명)
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

#파일 저장
# fig.savefig('text.png')
