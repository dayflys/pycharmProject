'''

    막대 그래프
    -plt.bar(x, 값) - 세로 막대그래프, x는 범주(종류), 값은 x에 해당되는 데이터 값
    -plt.barh() - 가로 막대그래프

     https://matplotlib.org/2.0.2/api/pyplot_api.html?highlight=bar#matplotlib.pyp lot.bar

    -> 막대 그래프는 두 개 이상 하나의 plot에 그리게 되면 뒤의 값이 더 클 때, 앞의 값을 덮어버리게 된다.

    - 멀티 막대 그래프를 사용시 기본적으로 막대 그래프가 겹쳐서 처리된다.
    따라서 값이 작은 그래프는 보이지 않는다.
    해결: stack 처럼 계속 쌓아서 처리 할 수 있다. ==> stacked bar 라고 부른다.
        plt.bar(..., bottom="") ==> 여러개 쌓을 수 있다.
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(3)
values1 = [100,200,300]
values2 = [200,150,50]
values3 = [20,10,23]

plt.bar(x,values1, label='values1')
plt.bar(x,values2, label='values2', bottom=values1)
plt.bar(x,values3, label='values3', bottom=values1)

plt.show()
