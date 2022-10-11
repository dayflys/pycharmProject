'''
    선그래프
    -plt.plot() 함수 이용
    -선(line) 또는 마커(marker, point) 그릴 때 사용

'''
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,4))

plt.plot([1,2,3,4],[1,4,9,16]) #x값, y값

plt.show()