'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용
    -라벨 지정
        xlabel(값), ylabel(값)

    - 선색상
        plt.plot(...,color="값")
        https://matplotlib.org/stable/tutorials/colors/colors.html#specifying-colors

    -marker 지정
        => x값과 y값이 만나는 지점에 point 지정
        https://matplotlib.org/stable/api/markers_api.html?highlight=marker#module-matplotlib.markers
        ==> marker 속성을 지정하지 않으면 선 없이 시각화
        ==> marker 속성을 지정하면 선+ marker 같이 시각화

    -선스타일
        plt.plot(..., linestyle='값')
'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration

fig,ax = plt.subplots(1,4)

ax[0].plot([1,2,3,4],[1,4,9,16], marker="P")
ax[1].plot([1,2,3,4],[1,4,9,16], "X")
ax[2].plot([1,2,3,4],[1,4,9,16], linestyle="--")
ax[3].plot([1,2,3,4],[1,4,9,16], color='g',marker="^",linestyle='--')

ax[0].set_xlabel('x label')#x 축 label
ax[0].set_ylabel('y label')#y 축 label
ax[3].set_xlabel('x label')#x 축 label
ax[3].set_ylabel('y label')#y 축 label

plt.show()