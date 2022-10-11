'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용
    -라벨 지정
        plt.xlabel(값), plt.ylabel(값)

    -축범위 지정
        plt.axis([xmin,xmax,ymin,ymax]) ===> 지정하지 않으면 데이터 값에 맞게 범위를 자동 지정
/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/matplotlib/mpl-data/matplotlibrc
'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration
plt.rc('font', family="Malgun Gothic")
plt.rc('font', size=15)
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(5,4))

plt.plot([1,2,3,4]) #x값,y값
plt.axis([0,10,0,20]) #[xmin,xmax,ymin,ymax]
plt.xlabel('x 값')#x 축 label
plt.ylabel('y 값')#y 축 label

plt.show()