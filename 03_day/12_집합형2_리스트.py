"""
    1.모든 데이터는 객체(클래스)
        1.일반형
            -정수
            -실수
        2.집합형
            -문자열
            -리스트
            -등등

    2.클래스
    class 클래스명:
        구성요소
            변수
            함수(메서드) <= 좀 중요
            -> 알아보기 위해서는 => print(dir(데이터 형))

    3. 함수
        1.builtin

    집합형
        리스트
        ->표현: [값1, 값2],list(iterable)
        -> 타입:type([10,20]) => <class 'list'>
                            => 리스트는 class 로 만들어짐
                            =>클래스 구성요소(변수, 함수)
        -> 특징: 순서가 있고 중복 허용 가능
            => 데이터 변경 가능한 mutable 한 특징(mutable sequence)
            => 인덱싱, 슬라이싱 사용 가능
        -> 함수 정리
        print(dir(list))
"""

#print(dir(list))

'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
  '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
   '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
     '__subclasshook__',
여기서 부터 함수
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
# #1.리스트 생성 방법
# str_list = ['홍길동','이순신']
# int_list = [10,20,30,30,30,100]
# mixed_list= [10,'이순신',3.14,True,None]
# nested_list1= [1,2,3,[9,8,7]]
# nested_list2= [[9,8,7],[1,2,3],[4,5,6]]
#
# str_to_list = list('hello')
# tuple_to_list = list((5,4,3))
# set_to_list = list({10,20,30})
# dict_to_list = list({'name':'뭐','age': 20})
# #help(list) #list(iterable=(),/)
# print(dict_to_list) # ['name', 'age']
# print(str_list) # ['홍길동', '이순신']
# print(int_list) # [10, 20, 30, 30, 30, 100]
# print(mixed_list) # [10, '이순신', 3.14, True, None]
# print(nested_list1) # [1, 2, 3, [9, 8, 7]]
# print(nested_list2) # [[9, 8, 7], [1, 2, 3], [4, 5, 6]]
# print(str_to_list) # ['h', 'e', 'l', 'l', 'o']
# print(tuple_to_list) # [5, 4, 3]
# print(set_to_list) # [10, 20, 30]

#2.
#가. append(값): 리스트에 추가
#list def append(self, __object: _T) -> None
m = [1,2,3]
m.append(100)
m.append(88)
m.append([4,3,2])

print('1. 리스트 안에 마지막 요소 추가: ', m) #1. 리스트 안에 요소 추가:  [1, 2, 3, 100, 88, [4, 3, 2]]
print()
#나. insert(값): 리스트의 지정된 위치에 값 추가
#list def insert(self,__index: SupportsIndex,__object: _T) -> None
m = [1,2,3]
m.insert(0,100) #일반형 삽입
print('2. 리스트 안에 지정된 위치에 요소 추가: ', m) #2. 리스트 안에 지정된 위치에 요소 추가:  [100, 1, 2, 3]
m.insert(0,[5,4,2])# 집합형 삽입
print('2. 리스트 안에 지정된 위치에 요소 추가: ', m) #2. 리스트 안에 지정된 위치에 요소 추가:  [[5, 4, 2], 100, 1, 2, 3]
m.insert(-1,777)#역방향도 가능하지만, -1 = 마지막요소 앞에 삽입된다. 맨 마지막 삽입은 append 로
print('2. 리스트 안에 지정된 위치에 요소 추가: ', m) #2. 리스트 안에 지정된 위치에 요소 추가:  [[5, 4, 2], 100, 1, 2, 777, 3]


# 다. extend(집합형) : 병합(merge) ==> 병합할 대상은 동등해야 된다. 집합형 대 집합형 (0) , 집합형 대 일반형(X)
# extend: list def extend(self, __iterable: Iterable[_T]) -> None
m = [1,2,3]
#m.extend(10) 집합형 vs 일반형 불가
m.extend([10])
print('3. 집합형 끼리 병합: ', m) #3. 집합형 끼리 병합:  [1, 2, 3, 10]
m.extend('hello')
print('3. 집합형 끼리 병합: ', m) #3. 집합형 끼리 병합:  [1, 2, 3, 10, 'h', 'e', 'l', 'l', 'o']
m.extend((4,3))
print('3. 집합형 끼리 병합: ', m) #3. 집합형 끼리 병합:  [1, 2, 3, 10, 'h', 'e', 'l', 'l', 'o', 4, 3]
#병합할 대상이 리스트로 한정이 된다면,extend 함수 대신 +(연결연산자)를 사용이 가능하다 , 파이썬에서는 요소 끼리의 합, 벡터 연산은 불가능
x= [1,2,3]
x2 = [9,8,7]
print(x+x2) #[1, 2, 3, 9, 8, 7]

#라. count: 포함 갯수
m = [1,2,3,4,2,3,2]
print('특정 단어 개수:',m.count(2)) #3
print("리스트 전체 갯수: ", len(m))#리스트 전체 갯수를 구할 때는 builtins 내장 함수인 len 함수를 사용한다.


# #마. index: 특정 값이 처음 나오는 위치값
# list def index(self,__value: _T,__start: SupportsIndex = ,__stop: SupportsIndex = ...) -> int
x= [1,2,3,5,30,5,2,2,8,9]
print('특정 값이 처음 나오는 위치 값:',x.index(2)) #특정 값이 처음 나오는 위치 값: 1
print('특정 값이 처음 나오는 위치 값:',x.index(2,3)) #특정 값이 처음 나오는 위치 값: 1

# 바. reverse: 집합형 요소들의 순서를 뒤바꿈, 자신이 거꾸로 변경된다. 원본이 변경된다
# 다만, builtins 객체의 reversed는 복사본을 만든다.

'''
    집합형 값을 거꾸로 변경하는 방법
    1.list의 reverse() 함수 사용
    ->list.reverse()
    ->list 자신이 거꾸로 변경됨
    
    2.builtins 객체의 reversed() 함수 사용
    -> reversed(리스트)
    -> 원본은 유지되고 거꾸로된 복사본은 반환한다.
'''
# list def reverse(self) -> None
m=[9,8,7,6,5]
print('집합형 요소들의 순서를 뒤바꿈:',m) #집합형 요소들의 순서를 뒤바꿈: (원본) [9, 8, 7, 6, 5]
m.reverse()
print('집합형 요소들의 순서를 뒤바꿈:',m) #집합형 요소들의 순서를 뒤바꿈: [5, 6, 7, 8, 9]

#reversed @overload def __init__(self, __sequence: Reversible[_T]) -> None
m2 = [9,8,7,6,5]
n = reversed(m2)# 그냥 출력하면 복사본의 주소값이 나옴 => list()함수를 사용하여 바꿔준다.
print('집합형 요소들의 순서를 뒤바꿈:',m2,n,list(n)) #집합형 요소들의 순서를 뒤바꿈: [9, 8, 7, 6, 5] <list_reverseiterator object at 0x1028c7f10> [5, 6, 7, 8, 9]

#사. 리스트의 요소 삭제: pop(인덱스), remove(값),clear()(전체삭제)
m=[9,8,7,6,5]
m.pop(0)
print('집합형 요소 삭제:',m) #[8, 7, 6, 5]
m.pop(-1)
print('집합형 요소 삭제:',m)#[8, 7, 6] 인덱스 값은 순방향, 역방향 다 가능하다.
#m.pop(10) #존재하지 않는 index 값 지정시 => IndexError 발생 => 삭제전 반드시 값이 존재하는지 확인 필수
m.remove(8)
m.insert(0,6)
m.remove(6)
if 100 in m:
    m.remove(100) #존재하지 않는 값 지정시 => ValueError => 삭제전 반드시 값이 존재하는지 확인 필수
else:
    pass
print('집합형 요소 삭제:',m)#[7] remove는 값을 하나만 왼쪽부터 삭제
m.clear()
print('집합형 요소 삭제:',m)#[] clear는 전체 삭제를 진행한다.

#아. 집합형의 요소를 정렬: sort #in-place = 자신이 변경되는 것
#list @overload def sort(self: list[SupportsLessThanT],*,key:(함수) None = ...,reverse: bool = ...) -> None

'''
    집합형 값을 정렬 방법(오름차순(default), 내림차순)
    1.list의 sort(key=함수, reverse=False ) 함수 사용
    ->list.sort(reverse=False) 오름차순
    ->list.sort(reverse=True) 내림차순
    ->list 자신이 정렬됨

    2.builtins 객체의 sorted() 함수 사용
    -> sorted_value = sorted(리스트) #오름차순
    -> 원본은 유지되고 정렬된 복사본을 반환한다.
'''

#가.수치정렬
m=[643,22,1,43,468,6]
print('집합형 요소들을 정렬:',m) #
m.sort()
print('집합형 요소들을 정렬:',m) #
m.sort(reverse=True)
print('집합형 요소들을 정렬:',m) #

#builtins @overload def sorted(__iterable: Iterable[_T],*,key: (_T) -> SupportsLessThan,reverse: bool = ...) -> list[_T]
m2 = [643,22,1,43,468,6]
sort_value = sorted(m2)# 그냥 출력하면 복사본의 주소값이 나옴 => list()함수를 사용하여 바꿔준다.
print('집합형 요소들을 정렬:',m2,sort_value,list(sort_value)) #집합형 요소들을 정렬: [643, 22, 1, 43, 468, 6] [1, 6, 22, 43, 468, 643] [1, 6, 22, 43, 468, 643] 오름차순
sort_value = sorted(m2,reverse=True)# 그냥 출력하면 복사본의 주소값이 나옴 => list()함수를 사용하여 바꿔준다.
print('집합형 요소들을 정렬:',m2,sort_value,list(sort_value)) #집합형 요소들을 정렬: [643, 22, 1, 43, 468, 6] [643, 468, 43, 22, 6, 1] [643, 468, 43, 22, 6, 1] 내림차순


# help(m.sort())
# help(sorted(m))

#나. 문자열 정렬
m = ["643","22","1","43","468","6"]
m.sort()
print(m) #[1, 6, 22, 43, 468, 643] -> 첫 글자로 정렬이 된 결과가 반환 됐다.
m.sort(reverse=True)
print(m) #['643', '6', '468', '43', '22', '1'] -> 첫 글자로 정렬이 된 결과가 반환 됐다.

m.sort(key=int)#key 값에는 함수 호출을 하면 안되고, 함수 이름을 적어줘야 한다.
print(m) #['1', '6', '22', '43', '468', '643']
m.sort(key=int,reverse=True)
print(m) #['643', '468', '43', '22', '6', '1']

#실습. 문자열 길이로 정리하기
m=['홍길동','세종대왕','정조']
m.sort(key=len)
print(m)#['정조', '홍길동', '세종대왕']


m = [1,2,3]
print(m*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3] => m 값이 세번 반복 되면서 하나의 리스트로 나온다.