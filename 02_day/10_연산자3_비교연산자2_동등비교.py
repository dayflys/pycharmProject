'''
    동등 비교
    1. == 연산자
        -> 값만 비교

    2. is 연산자
        -> 변수의 주소값을 비교하는 것

'''

a = 10
b = a
print(a==b) #True 변수에 들어있는 값이 같기 때문에 True가 출력된다.
print(a is b) #True -> 결국 값이 같이면 값에 해당하는 주소 값이 같기 때문에 True가 출력된다.
print(id(a), id(b), id(10))

n = [1,2,3]
n2 = n #n과 n2는 같은 주소값을 갖는다. 한쪽에서 값을 변경하면 다른쪽에 영향을 끼친다.
print(n == n2)
n[0]=100
print(n == n2)
print(n is n2)

a = [10,20]
b = a
print(a==b) #True
print(a is b) #True -> 다만 [10,20]과 주소 값이 다르다. 이를 보아 mutable 한 값은 다른 메모리 영역을 한번 거치는 것같다.
print(id(a), id(b), id([10,20]))

a = (10,20)
b = a
print(a==b) #True
print(a is b) #True -> 주소 값이 같다. 이를 보아 immutable 한 값은 바로 참조 하는 것으로 보인다.
print(id(a), id(b), id((10,20)))

a = {'name': '홍길동','age':10}
b = a
print(a==b) #True
print(a is b) #True
print(id(a), id(b), id({'name': '홍길동','age':10}))

'''
    python 특징
    -모든 data는 참조형 변수로 관리 (모든 변수는 참조형 변수) == sql의 외래키 (참조키)
    
    ** 자바
    -> 기본형
    -> 참조형
    
    ** 파이썬
    -> 일반형 => 기본형과 간접적으로 맵핑이 된다. 기본형 변수는 변수에 바로 값을 들어있는 것
    -> 집합형 => 참조형 변수와 간접적으로 맵핑이 된다. 참조형 변수는 변수에 주소값이 들어있는 것
'''


#복사본 생성
n = [1,2,3]
n2 = n[:]# n 의 index 0 부터 끝까지 n2에 복사하는 것, 이것도 n이 바뀌면 n2 도 바뀐다.
print(n == n2)# True
print(n is n2)# False
print(id(n), id(n2))

n = (1,2,3)
n2 = n[:]# n 의 index 0 부터 끝까지 n2에 복사하는 것
print(n == n2)# True
print(n is n2)# True
print(id(n), id(n2))

n= [1,2,3]
n2 = n.copy()
print(n == n2)#True
print(n is n2)#False
print(id(n), id(n2))

import copy

n = (1,2,3)
n2 = copy.deepcopy(n)
print(n == n2)#True
print( n is n2)#True
print(id(n), id(n2))


