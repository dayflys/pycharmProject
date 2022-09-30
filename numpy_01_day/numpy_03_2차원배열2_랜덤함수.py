'''
    랜덤값 이용
    1. 문법
     ->np.random.함수
'''
from pprint import pprint

import numpy as np


#1. np.random.random(), 0.0 <= < 1.0
print("1. np.random.random()") #def random(size: Any = None) -> None
print(np.random.random()) #스칼라 한개 반환 0.1915194503788923
print(np.random.random(5)) #갯수 1개: 1차원 벡터 반환 [0.86154418 0.23235626 0.88047038 0.16242597 0.04149824]
print(np.random.random((2,3))) #(행,열): 행렬 반환 [[0.92222627 0.59410343 0.15627715][0.96151134 0.6767712  0.39981437]]
print('*'*100)

#2. np.random.rand(), 균등 분포에서 랜덤값 추출
print("2. np.random.rand([갯수])") #def rand(*dn: Any) -> Any, 균등 분포에서 랜덤값 추출
print(np.random.rand()) # 스칼라 1개 반환: 0.2764642551430967
print(np.random.rand(5))# 벡터 반환:[0.80187218 0.95813935 0.87593263 0.35781727 0.50099513]
print(np.random.rand(2,3))# 행렬 반환(튜플값이 아닌, 행,열 로 넣어 준다 쉼표 구분자로) :[[0.20237256 0.50960539 0.81782903] [0.44089761 0.72858    0.31097686]]
print('*'*100)

#3. np.random.randn(), 표준 정규 분포(정규 분포중 평균값이 0이고 표준 편차가 1)에서 랜덤값 추출
print("4. np.random.randn([갯수])") #def randn(*dn: Any) -> float, 균등 분포에서 랜덤값 추출
print(np.random.randn()) #스칼라 1개 반환: 1.150035724719818
print(np.random.randn(5))#벡터 반환: [ 0.99194602  0.95332413 -2.02125482 -0.33407737  0.00211836]
print(np.random.randn(2,3))#행렬 반환: [[ 1.70164879 -0.47704515  0.45282997] [ 0.33595842  0.3631485   0.24315504]]
print('*'*100)

#4. np.random.randint(),
print("5. np.random.randint()")
print(np.random.randint(2)) #스칼라 1개 반환: 0
print(np.random.randint(2, size=5))#벡터 반환: [0 0 1 1 1]
print(np.random.randint(1,10, size=(2,3)))#행렬 반환: [[4 6 7] [7 5 3]]
print('*'*100)

#5. np.random.choice()
print("5. np.random.choice(리스트 ,size=(2,3))")
print(np.random.choice([3,6,8,9],size=(2,3)))
'''
[[9 3 3]
 [6 9 8]]
 '''
print('*'*100)