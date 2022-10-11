'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용
    -라벨 지정
        plt.xlabel(값), plt.ylabel(값)

    -축범위 지정
        plt.axis([xmin,xmax,ymin,ymax]) ===> 지정하지 않으면 데이터 값에 맞게 범위를 자동 지정

    -축범위 지정의 눈금 지정
        plt.xticks(리스트, label=리스트, rotation=각도)
        plt.yticks(리스트)

'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration
# plt.rc('font', family="DejaVuSans")
plt.rc('font', size=15)
plt.style.use('fivethirtyeight')

fig = plt.figure(figsize=(8,6))

plt.plot([1,2,3,4],[1,4,9,16]) #x값, y값

plt.xticks([1,2,3,4], labels=['1학년','2학년','3학년','4학년'], rotation=45)
plt.yticks([1,4,9,16], labels=['A','B','C','D'])

plt.xlabel('x label')#x 축 label
plt.ylabel('y label')#y 축 label

plt.show()