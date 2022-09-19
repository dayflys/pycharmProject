"""
    집합형
        셋
        ->표현: {값1, 값2},set(iterable)
        -> 타입:type({10,20}) => <class 'set'>
                            =>셋은 class 로 만들어짐
                            =>클래스 구성요소(변수, 함수)
        -> 특징: 순서가 없고, 중복 불가능
            => 저장되는 값은 immutable 한 값만 저장 된다
                => 따라서 리스트와 딕셔너리는 저장이 안된다.

            # 교집합(intersection), 차집합(difference), 합집합(union) -> 집합 연산자 기능 함수 제공(두드러진 특징)

        -> 함수 정리
        print(dir(set))
"""

# print(dir(set))
'''
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__'
, '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__'
, '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__'
, '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__'
, '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__'
, '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__'
, '__xor__'
여기서 부터 함수
, 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard'
, 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset'
, 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''

#1. 셋 생성 방법
m= {1,2,3,3,5,5}
m2 = set('hello')
m3 = set('helloHellO')
m4 = set([1,2,22,3,3,4,5,5])
print(m,m2,m3,m4) #{1, 2, 3, 5} {'h', 'e', 'l', 'o'} {'H', 'o', 'O', 'h', 'e', 'l'} {1, 2, 3, 4, 5, 22}

#immutable 데이터만 저장됨. mutable한 리스트 저장 불가
#m={3,4,4.3,True,(9,8,6),[5,4]} #TypeError

#2. 함수

m={1,2}
m.add(10)
m.add(3.15)
m.add(3.15)
m.add("hello")
#m.add([3,2,4]) #리스트는 저장 불가
m.add((3,2,4)) #{1, 2, 3.15, 10, 'hello', (3, 2, 4)}
print(m)
#help(m.add)

#나. update : 값 병합(집합형 대 집합형만 가능)
#set def update(self, *s: Iterable[_T]) -> None
m= {1,2}
m.update({3,4,5})
m.update((30,40,50))
m.update([300,400,500]) #병합은 안의 요소를 꺼내서 set을 만들기 때문에 리스트도 가능
print(m)#{1, 2, 3, 4, 5, 400, 30, 40, 300, 50, 500}
#m.update(999)

# help(m.update) #update(...)

#다. 삭제
m= {1,2,3,4,5}
#m.pop() #임의의 값 삭제, set이 비어있으면 => keyError 발생
#set def pop(self) -> _T
m.remove(3) #값으로 삭제, 값이 set안에 없으면=> keyError 발생
#set def remove(self, element: _T) -> None
m.discard(5) #값으로 삭제, 값이 set안에 없으면 => 아무것도 안 한다.
#set def discard(self, element: _T) -> None
print(m)
m.clear()# 값 모두 삭제
print('셋 길이:',len(m))

#라. 집합 연산자 교집합/합집합/차집합
n={1,2,3,4}
n2={2,3,5,6,7}

print('합집합:', n.union(n2)) #합집합: {1, 2, 3, 4, 5, 6, 7}
print('교집합:', n.intersection(n2)) #교집합: {2, 3}
print('차집합:', n.difference(n2)) #차집합: {1, 4}
print('차집합:', n2.difference(n)) #차집합: {5, 6, 7}

print('대칭 차집합:', n2.symmetric_difference(n)) #대칭 차집합: {1, 4, 5, 6, 7}: 합집합 - 교집합
print('대칭 차집합:', n.symmetric_difference(n2)) #대칭 차집합: {1, 4, 5, 6, 7}: 합집합 - 교집합
