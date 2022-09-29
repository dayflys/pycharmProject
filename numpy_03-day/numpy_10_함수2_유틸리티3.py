'''

    유틸리티 3
    1.   np.where(조건식) : 조건에 일치하는 인덱스 반환
         np.where(조건식, 참 , 거짓) : 3항 연산자 벡터화

    2.  np.unique(arr): 중복제거 하고 정렬해서 반환
        np.unique(arr, return_counts=True) : 중복제거하고 정렬해서 반환, 빈도수 반환
        np.unique(arr)[::-1]  : 내림차순 정렬

    3. np.choose( fancy 색인, arr): fancy 색인

    4. np.select(조건, 적용, 기본값) : 다중 조건 지정 가능

    5.  np.all() ===> 모두 참인지 여부
        np.any() ===> 하나라도 참인지 여부

        ===> True 와 False만 논리 값으로 사용되지 않고 다른 값도 논리값으로 사용이 가능하다.
            False로 처리: 0, "" ,None, [],{}

    6.np.fromstring(): split과 비슷, 문자열을 특정 구분자로 분리후 타입변경하고 ndarray로 반환

    7. 전치(transpose): 행과 열의 축 변경 후 복사본 반환 => 전치행렬을 의미함,transpose 함수 이용, arr.T 이용

    8. 행렬 곱(dot product) ==> 흔히 아는
        벡터 내적: 1차원인 벡터 간의 요소 곱의 합
        행렬곱: 행렬간 곱의 합

    9. np.clip(arr, 최소값, 최대값) ==> 지정된 최소값 보다 작은 값은 최소값으로 변경한다.
                     지정된 최대값 보다 큰 값은 최댓 값으로 변경한다.


'''

import numpy as np

#1.np.where(조건식): 조건과 일치하는 인덱스 반환
arr = np.array([9,8,7,6,5,4,3])
print("5값의 위치:", np.where(arr==5)) #5값의 위치 (array([4]),)
new_arr = np.delete(arr,np.where(arr==5))
print("5값 삭제 :", new_arr) #5값 삭제 : [9 8 7 6 4 3]

#2.np.where(조건식, 참, 거짓): 3항 연산자 벡터화 버전
arr = np.array([19,87,58,6,5,4,3])
print(arr%2 == 0) #[False False  True  True False  True False]
print("짝수면 -1 홀수면 0:", np.where(arr%2 == 0, -1, 0)) #짝수면 -1 홀수면 0: [ 0  0 -1 -1  0 -1  0]

#3.np.unique(arr): 중복 제거 후 정렬해서 새로운 arr 반환
arr = np.array([1,19,8,58,6,8,4,3,4,3])
print(arr) #[ 1 19  8 58  6  8  4  3  4  3]
print("np.unique : ", np.unique(arr)) #np.unique :  [ 1  3  4  6  8 19 58]
print("np.unique (최초의 arr의 오름차순지 인덱스 값): ", np.unique(arr, return_inverse=True)) #np.unique :  (array([ 1,  3,  4,  6,  8, 19, 58]), array([0, 5, 4, 6, 3, 4, 2, 1, 2, 1]))
print("np.unique (값의 갯수가 몇개인지): ", np.unique(arr, return_counts=True)) #np.unique :  (array([ 1,  3,  4,  6,  8, 19, 58]), array([1, 2, 2, 1, 2, 1, 1]))
print("np.unique : (최초의 arr의 요소에서 )", np.unique(arr, return_index=True)) #np.unique :  (array([ 1,  3,  4,  6,  8, 19, 58]), array([0, 7, 6, 4, 2, 1, 3]))

value, value_count = np.unique(arr, return_counts=True)
print(value,value_count) #[ 1  3  4  6  8 19 58] [1 2 2 1 2 1 1]
print(dict(zip(value,value_count))) #{1: 1, 3: 2, 4: 2, 6: 1, 8: 2, 19: 1, 58: 1}

#다차원 배열은 중복 제거후 flatten 됨
#이유는 중복 제거되는 시점에서 shape이 망가지기 때문이다.
arr2D = np.array([[1,4,4,8],[10,15,5,5]])
print('np.unique- 2차원:', np.unique(arr2D)) #np.unique- 2차원: [ 1  4  5  8 10 15]

#4. np.choose() :
arr = np.array(list('ABCDEFG'))
print(arr) #['A' 'B' 'C' 'D' 'E' 'F' 'G']
print(np.choose([0,1], arr)) #['A' 'B']
print('np.choose: ',np.choose([1,0,5], arr)) #['B' 'A' 'F']
print("fancy 색인: ",arr[[1,0,5]]) #['B' 'A' 'F']

#5 np.select(조건, 적용, 기본값) => 다중조건 지정 가능 => 조건과 적용이 1대 1 대응 된다. 조건이 만족하지 않는다면 default 값이 출력된다.
x = np.arange(10)
print(x)#[0 1 2 3 4 5 6 7 8 9]
condlist = [x < 3 , x > 5]
choicelist = [x+100, x-100]
print(np.select(condlist,choicelist,0))

#6. np.all(), np.any()

#가. True와 False 값이 아닌 다른 값을 논리값으로 처리한 형태
arr = np.array([0,0,0]) #False
arr = np.array([1,1,1]) #True
arr = np.array([1,1,0]) #False
print(np.all(arr))

arr = np.array([True,True,True]) #True
arr = np.array([False,False,False]) #False
print(np.all(arr))

#응용
a = np.array([1,2,3,4])
b = np.array([4,3,2,4])
print("a배열 값이 b배열 값보다 모두 크냐?", a > b) #[False False  True  True]

print(np.all(a > b)) #False

#np.all(arr) 하고 arr.all()는 결과가 동일 하다.
arr = np.array([1,1,1])
print(np.all(arr)) #True
print(arr.all()) #True

#np.any()
print("a배열 값이 b배열 값보다 하나라도 크냐?", np.any(a > b)) #a배열 값이 b배열 값보다 하나라도 크냐? True
print("a배열 값이 b배열 값보다 하나라도 같냐?", np.any(a == b)) #a배열 값이 b배열 값보다 하나라도 같냐? True
arr = np.array([1,1,1])
print(np.any(arr)) #True
print(arr.any()) #True

#7. np.fromstring() ==> 문자열을 특정 구분자로 분리후 타입변경하고 ndarray로 반환
data = "10:20:30"
print(np.fromstring(data,dtype=np.int32, sep=":" )) #[10 20 30] => 반환은 ndarray로 반환된다.

data = "10,20,30"
print(np.fromstring(data,dtype=np.int32, sep="," )) #[10 20 30] => 반환은 ndarray로 반환된다.

data = "10 20 30"
print(np.fromstring(data,dtype=np.int32, sep=" " )) #[10 20 30] => 반환은 ndarray로 반환된다.

#8. 전치 ==> transpose 함수 이용, arr.T 이용
arr = np.arange(15).reshape(3,5)
print(arr)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
 '''
print(np.transpose(arr))
'''
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
# '''
print(arr.T)
'''
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
 '''

# s = np.array("hello")
# print(dir(s))
'''
['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__'
, '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__'
, '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__'
, '__class_getitem__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__'
, '__delitem__', '__dir__', '__divmod__', '__dlpack__', '__dlpack_device__', '__doc__'
, '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__'
, '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__'
, '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__'
, '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__'
, '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__'
, '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__'
, '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__'
, '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__'
, '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__'
, '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__'

, 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base'
, 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes'
, 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill'
, 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max'
, 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp'
, 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield'
, 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take'
, 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
'''

#9. 내적: 1차원인 벡터간의 곱하고 합 연산
arr = np.arange(5)
print(arr) #[0 1 2 3 4]
print(np.dot(arr,arr)) #30 0*0+1*1+2*2+3*3+4*4

#10 행렬곱: 2차원 행렬 곱의 합 연산
arr = np.arange(4).reshape(2,2)
arr2 = np.arange(5)
print(arr)
'''
[[0 1]
 [2 3]]
'''
print(np.dot(arr,arr))
'''
[[ 2  3]
 [ 6 11]]
 '''
# print(np.dot(arr,arr2)) # 앞 행렬과 뒤 행렬의 dimension이 맞아야 한다.

#10. np.clip(arr,최소값, 최대값) => 지정된 최소값 보다 작은 값은 최솟값으로 지정된 최댓값보다 큰 값은 최댓값으로 변경한다.
arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print(np.clip(arr,4,7)) #[4 4 4 4 4 5 6 7 7 7]