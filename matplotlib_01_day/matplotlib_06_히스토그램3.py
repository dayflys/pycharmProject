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
np.random.seed(1234)
a= np.random.randn(1000)+1
b= np.random.randn(1000)
c= np.random.randn(1000)-1

plt.hist(a, bins=20, alpha=0.5, label="A") #bins는 몇개의 영역으로 쪼갤지 설정, density=True 지정시 밀도함수가 되어 면적이 1
plt.hist(b, bins=20, alpha=0.5, label="B")
plt.hist(c, bins=20, alpha=0.5, histtype='step',label="C") #histtype='step'지정하면 막대내부가 비워짐
plt.show()
