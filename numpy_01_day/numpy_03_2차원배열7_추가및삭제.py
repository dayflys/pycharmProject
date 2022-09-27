'''

    배열 추가 및 삭제

    1. 추가
        new_arr = np.append(원본, 추가할 데이터(리스트포함), axis=None|0|1)
        -> 새로 추가된 배열이 만들어진다.
        => axis=None이면 flat 된후 추가 된다.
        => axis=0이면 행이 추가가 된다.(주의할 점: dimension이 일치해야 한다.)
        => axis=1이면 열이 추가가 된다.(주의할 점: dimension이 일치해야 한다.)
    2.삽입
        new_arr = np.insert(arr, 위치(idx|fancy|slice), 값)
        new_arr = np.insert(arr, [위치, 위치2], [위치의 값, 위치2의 값])

'''
import numpy as np

arr = np.arange(6).reshape(-1,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]]
'''
print('*'*100)
#가. axis=None ==> flat된 후 처리됨.
#1.idx 추가
new_arr = np.append(arr,100)
new_arr = np.append(arr,[100])
print(new_arr) #[  0   1   2   3   4   5 100]
print('*'*100)
#나. axis=0 ===> 행이 추가가 된다.
#1.idx 추가
#2차원 배열에 행을 추가 할때는 2차원 형태로 지정해야 한다.
# new_arr = np.append(arr,[100,200,300], axis=0)
#ValueError:
# all the input arrays must have same number of dimensions,
# but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
new_arr = np.append(arr,[[100,200,300]], axis=0)
print(new_arr) #[[  0   1   2] [  3   4   5] [100 200 300]]
new_arr = np.append(arr,[[100,200,300],[1,2,3],[999,877,666]], axis=0)
print(new_arr) #[[  0   1   2][  3   4   5][100 200 300][  1   2   3] [999 877 666]]
print('*'*100)
#다. axis=1 ===> 열이 추가가 된다.
#1.idx 추가
#2차원 배열에 열을 추가 할때는 2차원 형태로 지정해야 한다.
new_arr = np.append(arr,[[100],[200]], axis=1)
print(new_arr) #[[  0   1   2 100] [  3   4   5 200]]
new_arr = np.append(arr,[[100,99,88],[200,199,198]], axis=1)
print(new_arr) #[[  0   1   2 100  99  88] [  3   4   5 200 199 198]]
print('*'*100)


#2. np.insert(ndarray,위치, 값)
#가. axis=None
new_arr = np.insert(arr, 0, 100)
print(new_arr) #[100   0   1   2   3   4   5]

#나. axis=0
#브로드캐스팅(broadcasting) ==> 연산하기 위해서 갯수를 자동으로 증가시키는 것.
new_arr = np.insert(arr, 0, 99, axis=0)
print(new_arr) #[[99 99 99] [ 0  1  2] [ 3  4  5]]

#다. axis=1
#브로드캐스팅(broadcasting) ==> 연산하기 위해서 갯수를 자동으로 증가시키는 것.
new_arr = np.insert(arr, 0, 98, axis=1)
print(new_arr) #[[98  0  1  2] [98  3  4  5]]
