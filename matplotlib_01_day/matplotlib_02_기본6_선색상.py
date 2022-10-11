'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용
    -라벨 지정
        xlabel(값), ylabel(값)

    - 선색상
        plt.plot(...,color="값")
        https://matplotlib.org/stable/tutorials/colors/colors.html#specifying-colors
'''
import matplotlib

import matplotlib.pyplot as plt
#runtime configuration

fig = plt.figure(figsize=(5,4))

plt.plot([1,2,3,4],[1,4,9,16], color='r')
plt.plot([3,4,8,9],[1,4,9,16], color="blue")
plt.plot([7,4,3,6],[1,4,9,16], "g")

plt.xlabel('x label')#x 축 label
plt.ylabel('y label')#y 축 label

plt.show()