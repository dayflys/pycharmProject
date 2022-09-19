"""
    집합형
        튜플
        ->표현: (값1, 값2),tuple(iterable)
            ->값 하나의 튜플은 (10,) 쉼표를 찍어주어야 한다.
        -> 타입:type((10,20)) => <class 'tuple'>
                            => 튜플은 class 로 만들어짐
                            =>클래스 구성요소(변수, 함수)
        -> 특징: 순서가 있고 중복 허용
            => 데이터 변경 불가능한 immutable 한 특징(immutable sequence
            => 인덱싱, 슬라이싱 사용 가능
        -> 함수 정리
        print(dir(tuple))
"""

# print(dir(tuple))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__'
, '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
, '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__'
, '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__'
, '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__'
, '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
여기서 부터 함수
, 'count', 'index']
'''

#1. 튜플 생성
m= (1,3,4,5,5,5,7)
m2 = (100,)
m3 = tuple([1,2,3])
m4 = tuple('hello')
print(m,m2,m3,m4) #(1, 3, 4, 5, 5, 5, 7) (100,) (1, 2, 3) ('h', 'e', 'l', 'l', 'o')

# 주의: tuple은 값 변경(immutable) => 리스트에서 제공되었던 수정 함수들이 제공 안됨.(append, insert,remove, pop ,clear 안됨)
#m[0] = 100 # TypeError 발생

#2.함수
#count - 특정 문자의 개수 반환
m = (1,3,4,5,5,5,7)
print(m.count(5)) # 3
print("tuple의 전체 개수:", len(m)) #tuple의 전체 개수: 7

#index: 특정문자의 처음나오는 위치값 반환
print(m.index(3)) # 1


m = (1,2,3)
print(m*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3) => m 값이 세번 반복 되면서 하나의 리스트로 나온다.