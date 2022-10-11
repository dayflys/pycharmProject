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
'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration

fig = plt.figure(figsize=(5,4))

plt.plot([1,2,3,4],[1,4,9,16], marker="P") #marker 지정
plt.plot([3,4,8,9],[1,4,9,16], "D") #marker 지정
plt.plot([1,3,6,15],[1,4,9,16], "bX") #marker와 color 같이 지정

plt.xlabel('x label')#x 축 label
plt.ylabel('y label')#y 축 label

plt.show()