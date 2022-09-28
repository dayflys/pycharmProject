'''

    1차원 배열(벡터) 색인
    1) 인덱싱, 슬라이싱 (기존 파이썬 문법과 동일)
        -기본적으로 위치값을 이용
        -순방향
        -역방향

    2) fancy 색인 (정수배열 색인)
    -한꺼번에 여러 값 색인
    -반드시 배열에 담아서 전달 해야한다.
    -임의의 순서 지정 가능
    -역방향도 가능
    -지정한 순서대로 출력됨

    3) boolean 색인
    - 벡터 연산 중에서 비교 연산 활용
    - 반드시 길이가 같아야 한다.
'''

# 4. boolean 색인
import numpy as np
arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print(arr[[True,True,True,True,True,False,False,False,False,False]]) #[0 1 2 3 4]
print("짝수냐", arr%2 == 0) #짝수냐 [ True False  True False  True False  True False  True False]
print("짝수만 출력: ", arr[arr%2 == 0]) #짝수만 출력:  [0 2 4 6 8]
print("5보다 큰 값만 출력: ", arr[arr > 5]) #5보다 큰 값만 출력:  [6 7 8 9]
print("5보다 크고 짝수냐 출력: ", arr[(arr%2 == 0)  & (arr > 5)]) #5보다 크고 짝수냐 출력:  [6 8]
print("5보다 크거나 짝수냐 출력: ", arr[(arr%2 == 0) | (arr > 5)]) #5보다 크거나 짝수냐 출력:  [0 2 4 6 7 8 9]
