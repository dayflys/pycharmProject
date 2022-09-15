'''
    1. packing
        값1, 값2, .... => 집합형으로 데이터들을 묶는 것
        => 대표적으로 [],()로 묶는다
    2. unpacking ===> *집합형 (dictionary는 제외)
        집합형 => 개별적인 값으로 풀어 헤치는 것을 의미
        집합형 => 값1,값2,...
        ----> dictionary는 **dict로 unpacking해야한다.
        =>이때 출력은 별칭을 사용한 '{key}'.format(key='value')처럼 출력된다.
'''

print('hello')#hello 출력
print(*'hello')#h,e,l,l,o 출력

print([10,20,30])#[10,20,30] 출력
print(*[10,20,30])#10,20,30 출력
#2. "{},{},...".format(*값(집합형))

x = [10,20,30]
mesg = "값1:{} , 값2:{}, 값3:{}".format(x[0],x[1],x[2])
print(mesg)
mesg = "값1:{} , 값2:{}, 값3:{}".format(*x)
print(mesg)

#3. "{},{}".format( dict ) -> 이것은 mesg ="값1: {name} 값2:{age}".format(name='홍길동',age = 20)와 동일하게 출력된다.
y = {'username': '홍길동', 'age': 20}
mesg = "값1:{username} , 값2:{age}".format(**y)
print(mesg)
