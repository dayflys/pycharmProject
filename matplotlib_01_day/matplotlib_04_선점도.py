'''

    산점도( scatter plot)
    - 두 변수간의 상관관계를 그래프의 점으로 표현하는 그래프
    - 상관관계 - 분산된 점 위로 경양성을 나타내는 선을 그엇을 때 알아볼 수 있는 것
        - 양의 상관관계 = x가 증가 할때 y가 증가하는 것 => 가장 좋은 값 : 1
        - 음의 상관관계 = x가 증가 할때 y가 감소하는 것 => 가장 좋은 값 : -1
        - 상관 계수의 절댓값이 1에 가까울 수록 두 변수의 상관 관계가 크다고 볼 수 있다.
    - plt.scatter(x,y, s=point크기, c=색상, alpha=투명도)
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = (30*np.random.rand(N))**2
colors = np.random.rand(N)

plt.scatter(x,y, s=area, c=colors, alpha=0.3)
plt.show()
