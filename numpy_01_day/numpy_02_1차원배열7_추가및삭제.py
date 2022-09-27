'''

    배열 추가 및 삭제

    1. 추가
        new_arr = np.append(원본, 추가할 데이터(리스트포함))
        -> 새로 추가된 배열이 만들어진다.

    2.삽입
        new_arr = np.insert(arr, 위치(idx|fancy|slice), 값)
        new_arr = np.insert(arr, [위치, 위치2], [위치의 값, 위치2의 값])

'''
import numpy as np

#1. np.append(ndarray, 값)
print("1. np.append(ndarray, 값)")
arr = np.array([9,8,7,6,5,4,3])
new_arr = np.append(arr, 10)
print(new_arr, arr) #[ 9  8  7  6  5  4  3 10] [9 8 7 6 5 4 3] => 추가 된 값은 마지막단 요소로 들어간다.
new_arr = np.append(arr, [1,2,3])
print(new_arr, arr) #[9 8 7 6 5 4 3 1 2 3] [9 8 7 6 5 4 3]
new_arr = np.append(arr, np.array([6,5,43,32]))
print(new_arr, arr) #[ 9  8  7  6  5  4  3  6  5 43 32] [9 8 7 6 5 4 3]


#2. np.insert(ndarray,위치, 값) => indexing, fancy, slicing이 모두 가능하다.
print("2. np.insert(ndarray,위치, 값)")
arr = np.array([9,8,7,6,5,4,3])
new_arr = np.insert(arr, 0, 100)
print(new_arr, arr) #[100   9   8   7   6   5   4   3] [9 8 7 6 5 4 3]
new_arr = np.insert(arr, [0,2],900)
print(new_arr, arr) #[900   9   8 900   7   6   5   4   3] [9 8 7 6 5 4 3]
new_arr = np.insert(arr, np.s_[0:3],900) #
print(new_arr, arr) #[900   9 900   8 900   7   6   5   4   3] [9 8 7 6 5 4 3]
new_arr = np.insert(arr, [0,3],[1,2])
#특정위치에 특정 값 일대일 대응해서 저장
print(new_arr, arr) #[1 9 8 7 2 6 5 4 3] [9 8 7 6 5 4 3]
