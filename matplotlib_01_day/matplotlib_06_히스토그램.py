'''

    히스토그램
    1) 도수분포표: 특정 구간에 속하는 자료의 개수를 표로 표현한 것
    2) 히스토그램: 도수분포표를 시각화한 그래프

'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

weight = [68,81,64,56,78,61,77,66,68,59,71,80,59,67,81,69,74,70,65]
plt.hist(weight)
plt.show()
