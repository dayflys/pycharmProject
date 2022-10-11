'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용
    -라벨 지정
        xlabel(값), ylabel(값)

'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration
print(matplotlib.matplotlib_fname())
plt.rc('font', family="Malgun Gothic")
plt.rc('font', size=15)
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(5,4))

plt.plot([1,2,3,4]) #y값
plt.xlabel('x 값')#x 축 label
plt.ylabel('y 값')#y 축 label

plt.show()