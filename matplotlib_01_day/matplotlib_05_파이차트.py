'''

    파이 차트 (pie chart)
    -범주(종류)의 구성 비율을 원형으로 표현한 그래프이다.
    - 비율의 총합은 100이 되어야 한다.

    -ratio: 각 변수가 차지하는 비율 => 전체 합이 100이 되어야 한다.
    -labels : 각 변수의 이름
    -autopct: 차지하는 비율을 퍼센트로 나타냄
    => 파이 차트는 기본적으로 0도 부터 시계 반대방향으로 그려진다
        => 시작점과 방향은 커스터마이징이 가능하다.
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ratio = [34,32,16,18]
labels = ['Apple','Banana','Melon','Grapes']

plt.pie(ratio, labels=labels, autopct="%1.1f%%")
plt.show()
