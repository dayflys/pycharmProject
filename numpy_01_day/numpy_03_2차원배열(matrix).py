'''
    정리
    1.방법 두가지
        가. np.array(중첩리스트) 이용해서 2차원 배열(행렬) 생성이 가능하다.
            ==> 반드시 열의 개수는 일치해야 한다.
        나. arr = np.array(1차원리스트) and arr.shape= (행,열)
            => shape을 이용해서 모양을 바꾼다. (행, 열)
            => (행, -1) # 지정된 행의 갯수에 의해서 열 갯수가 설정된다
            => (-1, 열) # 지정된 열의 갯수에 의해서 행 갯수가 설정된다
    2. 반드시 동일한 타입을 지정해야 한다. 타입이 다르면 일치시킨다. (upcasting : 데이터 크기가 큰 것으로 일치 시킨다.)
    3. 정수는 기본이 4byte인 int32이고 실수는 기본이 8byte인 float64dlek.
    4. 차원 정보는 ndim, 모양은 shape으로, 저장된 데이터 타입은 dtype으로 알 수 있다.
'''
#1. 2차원 배열인 행렬 생성, 문법: np.array(중첩 리스트)
import numpy as np

# x = [[1,2,3],[4,5,6,7]]
'''
VisibleDeprecationWarning
: Creating an ndarray from ragged nested sequences 
(which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes)
is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
deprecated? => 과거에는 사용이 되었지만, 현재는 사용이 안된다는 말이다 ===> 언제든지 지원 안할 수 있음을 암시한다.
'''
x = [[1,2,3],[4,5,6]]
s = np.array(x)
print(x, s)#[[1, 2, 3], [4, 5, 6]] [[1 2 3] [4 5 6]]
print(type(x),type(s)) #<class 'list'> <class 'numpy.ndarray'>
print(s.ndim, s.shape) #2 (2, 3) => 차원 수는 2차원, shape은 튜플 형식으로 출력된다.
print(s.dtype) #int64 => dtype은 저장되는 데이터 타입을 알 수 있다.

#2. 2차원 배열인 행렬 생성, 문법: np.array(리스트).shape 1차원 ----> 2차원
arr = np.array(np.arange(10))
print(arr) #[0 1 2 3 4 5 6 7 8 9]
#1차원 ===> 2차원 # 행 * 열 = arr의 요소갯수 와 일치하여야한다.
#명시적으로 행과 열 지정
arr.shape = (1,10)
print(arr) #[[0 1 2 3 4 5 6 7 8 9]]
arr.shape = (2,5)
print(arr) #[[0 1 2 3 4][5 6 7 8 9]]
arr.shape = (5,2)
print(arr) #[[0 1][2 3][4 5][6 7][8 9]]
arr.shape = (10,1)
print(arr) #[[0][1][2][3][4][5][6][7][8][9]]

#묵시적으로 행과 열 지정
arr.shape = (2,-1) #(2,5) 동일
print(arr) #[[0 1 2 3 4] [5 6 7 8 9]]
arr.shape = (-1, 10) #(1,10) 동일
print(arr) #[[0 1 2 3 4 5 6 7 8 9]]


