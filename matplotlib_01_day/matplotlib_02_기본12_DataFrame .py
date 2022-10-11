'''
    DataFrame의 데이터 이용해서 시각화

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

google = pd.read_csv('./dataset/GOOGL_data.csv')
amazon = pd.read_csv('./dataset/AMZN_data.csv')
# print(google.head())
# print(amazon.head())

fig = plt.figure(figsize=(16,8))
plt.plot('date','close',data=google, label='google')
plt.plot('date','close',data=amazon, label='amazon')

plt.xticks(np.arange(0,1260,40), rotation=70)
plt.xticks(np.arange(0,1450,100))

plt.title('stock price')
plt.xlabel('date')
plt.ylabel('price')
plt.legend()
plt.show()