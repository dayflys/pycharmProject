"""
    1.zip 함수
        -builtins 객체에 제공하는 함수
        -서로 분리된 리스트를 하나로 묶어 준다.
        -dict(zip(리스트,리스트))로 딕셔너리로 만들어 준다.

    2.dict 출력을 가독성 있게 하기

"""

x = ['a', 'b', 'c']
y = [10,20,30]
n = zip(x,y)
print(n) #<zip object at 0x104e34440>
print(dict(n)) #{'a': 10, 'b': 20, 'c': 30}
print(dict(zip(y,x))) #{10: 'a', 20: 'b', 30: 'c'}

#가독성 있게 출력해주는 패키지
from pprint import pprint as p
m = {'a':300,'b': [3400,2234,456,666], 'c':{'c1':2345243,'c2':[234234]},'d':{'d1':2345243,'d2':[234234]}}
p(m)
