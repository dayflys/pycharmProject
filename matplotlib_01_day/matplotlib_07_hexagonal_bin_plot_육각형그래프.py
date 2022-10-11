'''

    육각형 그래프(hexagonal_bin_chart) (vs 산점도)
    - scatter(산점도)의 단점을 보완한 그래프임
    - plt.hexbin(x,y, gridsize=육각형의 개수)


'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(1234)

df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
df['b'] = df['b']+np.arange(1000) #뒤로 갈수록 'b' 값이 커진다.

fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(17,6))
ax[0].scatter(df['a'],df['b'])
ax[1].hexbin(df['a'],df['b'])
ax[2].hexbin(df['a'],df['b'],gridsize=50)
ax[3].hexbin(df['a'],df['b'],gridsize=50, cmap='Blues')
ax[4].hexbin(df['a'],df['b'],gridsize=50, cmap='Blues', alpha=0.4)

plt.show()
