'''
    정리
    1. np.array(리스트) 이용해서 1차원 배열(벡터) 생성이 가능하다.
    2. 반드시 동일한 타입을 지정해야 한다. 타입이 다르면 일치시킨다. (upcasting : 데이터 크기가 큰 것으로 일치 시킨다.)
    3. 정수는 기본이 4byte인 int32이고 실수는 기본이 8byte인 float64dlek.
    4. 차원 정보는 ndim, 모양은 shape으로, 저장된 데이터 타입은 dtype으로 알 수 있다.
'''
#1. 1차원 배열인 벡터 생성, 문법: np.array(리스트| 튜플)
import numpy as np

x = [1,2,3]
s = np.array(x)

print(x, s)#[1, 2, 3] [1 2 3] => 파이썬의 리스트는 쉼표 구분자가 있고, 없다면 ndarray로 만들어진 vector 이다.
print(type(x),type(s)) #<class 'list'> <class 'numpy.ndarray'>
#print(x.ndim, x.shape) => 파이썬에서의 리스트는 파이썬 list 타입이므로 ndim과 shape이라는 속성이 없다
print(s.ndim, s.shape) #1 (3,) => 차원 수는 1차원, shape은 튜플 형식으로 출력된다.
print(s.dtype) #int64 => dtype은 저장되는 데이터 타입을 알 수 있다.

'''
    int8: -127 ~128
    int16: -32768~32767
    int32: -2,147,483,648 ~ 2,147,483,647
    int64: -9223372036854775808~9223372036854775807
'''

#2.1 차원 배열인 벡터 생성, np.array(리스트) numpy의 배열은 반드시 동일한 타입으로 저장한다. 만약 타입이 다르면 동일한 타입으로 일치시킨다.
x = [1,2,3,"A"]
y = ["a"]
s = np.array(x)  # numpy는 요소의 데이터 타입이 통일 된다.
s1 = np.array(y)  # numpy는 요소의 데이터 타입이 통일 된다.
print(x, s) #[1, 2, 3, 'A'] ['1' '2' '3' 'A']
print(s.ndim, s.shape, s.dtype) #1 (4,) <U21
print(s1.dtype) #<U1 => 유니 코드를 나타낸다.

x = [1,2,3,100.]
s = np.array(x)
print(x, s) #[1, 2, 3, 100.0] [  1.   2.   3. 100.]
print(s.ndim, s.shape, s.dtype) #1 (4,) float64 -> 정수는 4byte가 기본이고 실수는 8byte가 기본이다.

x = ['A','B', 'C', 'D']
x = ['AA','BB', 'C', 'D']
x = ['AAA','BB', 'C', 'D']
s = np.array(x)
print(x, s) #['A', 'B', 'C', 'D'] ['A' 'B' 'C' 'D']
print(s.ndim, s.shape, s.dtype) #1 (4,) <U3 => U 다음에 나오는 것은 문자의 최대 갯수이다.