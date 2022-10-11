'''

    막대 그래프
    -plt.bar(x, 값) - 세로 막대그래프, x는 범주(종류), 값은 x에 해당되는 데이터 값
    -plt.barh() - 가로 막대그래프

     https://matplotlib.org/2.0.2/api/pyplot_api.html?highlight=bar#matplotlib.pyp lot.bar
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(3)
values = [100,200,300]

plt.bar(x,values)

plt.show()
