'''

    히스토그램
    1) 도수분포표: 특정 구간에 속하는 자료의 개수를 표로 표현한 것
    2) 히스토그램: 도수분포표를 시각화한 그래프
        -plt.hist()
        -bins=구간을 몇개로 나눌 건지의 값, default=10
        -histtype= 히스토그램을 어떤 형태로 출력 할 것인지를 결정한다.

'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

weight = [68,81,64,56,78,61,77,66,68,59,71,80,59,67,81,69,74,70,65]
fig, ax = plt.subplots(nrows=1,ncols=5)
ax[0].hist(weight)
ax[1].hist(weight, bins=5)
ax[2].hist(weight, bins=20)
ax[3].hist(weight, histtype="step")
ax[4].hist(weight, histtype='bar', fill=False)
plt.show()
