'''

    박스 그래프 (box chart)
    -용도:
        데이터의 범위(최대, 최소, 중앙값) 및 이상치(outlier) 식별용.

    -구현:
        데이터 값을 동일한 비율의 4개로 구분

    1번      2번      3번      4번
       1사분위   2사분위    3사분위
               (중앙값)
          |---------------|
            IQR(Inter Quartile range)

    최대값: 3사분위값 + 1.5*IQR
    최대값: 1사분위값 - 1.5*IQR
    ==> 최대값 및 최소 값을 벗어나는 데이터를 이상치(outlier)로 처리한다.



'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(1234)

x = np.random.random(9)

print(sorted(x, reverse=True))
# plt.show()
iqr = np.quantile(x,0.75)-np.quantile(x,0.25)
print("1사분위:" , np.quantile(x,0.25)) #1사분위: 0.2764642551430967
print("2사분위:" , np.quantile(x,0.5)) #2사분위: 0.6221087710398319
print("3사분위:" , np.quantile(x,0.75)) #3사분위: 0.7853585837137692
print("IQR:" , iqr) #IQR: 0.5088943285706725
print("최댓값:" ,np.quantile(x,0.75)+ 1.5*iqr) #최댓값: 1.5487000765697778
print("최소값:" ,np.quantile(x,0.25)- 1.5*iqr) #최소값: -0.486877237712912

plt.boxplot([x,x,x])
plt.show()
