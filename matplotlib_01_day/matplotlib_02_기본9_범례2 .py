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

    -범례(legend)
    가.
        plt.plot(...,label='값1')
        plt.plot(...,label='값2')

        plt.legend()
    나.
        plt.legend([리스트])===> plot 순서대로 범례가 적용이 된다.


'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration

fig = plt.figure(figsize=(8,6))

plt.plot([1,2,3,4],[1,4,9,16], color='r')
plt.plot([3,4,8,9],[1,4,9,16], color="blue")
plt.plot([7,4,3,6],[1,4,9,16], "g")

plt.xlabel('x label')#x 축 label
plt.ylabel('y label')#y 축 label
plt.legend(["AAA","BBB","CCC"])
plt.show()