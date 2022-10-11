'''

    파이 차트 (pie chart)
    -범주(종류)의 구성 비율을 원형으로 표현한 그래프이다.
    - 비율의 총합은 100이 되어야 한다.
    -plt.pie()
    -기본적으로 0도부터 시계 반대방향으로 그래프를 그린다
    -startangle 값이 시작 각도를 의미한다.
    -counterclock=False로 지정하면 시계 방향으로 영역이 표시됨
    -colors = 리스트 로 색상지정
    -explode=리스트 로 지정된 값만큼(0.1 ==> 10%) 원에서 해당 부채꼴을 분리 시킨다.

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
colors=['#ff9999','#ffc000','#8fd9b6','#d395d0']
explode = [0,0.1,0,0]

plt.pie(ratio, labels=labels, autopct="%1.1f%%", startangle=240, counterclock=False, colors=colors, explode=explode)
plt.show()
