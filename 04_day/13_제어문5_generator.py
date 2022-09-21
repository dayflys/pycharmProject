'''

    generator
    -특징: 한번에 한개만 생성 => memory 관리 효율적 -> memory에 한 개 요소씩 할당
    -next()함수를 이용해서 값얻기
    -for 문 이용해서 값 얻기
    -대표적인 generator는 range()
    -(x for x in range(5))<= 커스텀 generator, 사용자 지정 generator

    generator
    -한 번에 한 개의 항목만 생성됨(메모리 유지 x)
    생성된 항목을 사용하면 제거됨.
    -ramdom access가 불가 하다.
    -next()함수 또는 for 문을 사용해서 값을 얻을 수 있다.
    -커스텀 generator는 다음 문법을 이용한다.

    gen = ( 표현식 for 변수 in 리스트)
    - next(gen) 형식으로 값을 하나씩 얻는다.
    - for v in gen:
        print(v)

'''

#list comprehension vs generator

x = [ v for v in range(5)]
print(x)#[0, 1, 2, 3, 4]
y = ( v for v in range(5))
print(y) #<generator object <genexpr> at 0x104b21f50> <- 이 결과가 나오면 generator 로 출력됐다는 것을 인지하자.
print('*'*40)
print(x[0])#0
print(x[1])#1
print(x[2])#2
print(x[3])#3
print(x[4])#4
print(x[0])#0
print('*'*40) #리스트는 값을 뽑아 와도 다시 뽑을 수 있다. 메모리에 올라가 있기 때문이다.
print(next(y)) #0
print(next(y)) #1
print(next(y)) #2
print(next(y)) #3
print(next(y)) #4
# print(next(y)) #generator는 값을 반환하면 제거하기 때문에 이 코드는 오류가 나고 다시 값을 얻으려면 generator를 다시 만들어야 한다.
# 에러 발생. 이전에 항목을 모두 소진했기 때문이다.

y = ( v for v in range(10,16))
for v in y:
    print(v, end=' ') #10 11 12 13 14 15

'''
    range() generator
    1. next() 값 얻기
'''

z = range(5)
print(z)#range(0, 5)
print(list(z))#[0, 1, 2, 3, 4]

#print(next(z))#TypeError: 'generator' object is not subscriptable
#반복 가능한 iterator로 만들고 next() 하면 된다.
#-> 방법은 builtins 객체의 iter함수를 사용
print(next(iter(z)))#0
print(next(iter(z)))#0
print(next(iter(z)))#0

z_iter = iter(z)
print(next(z_iter))#0
print(next(z_iter))#1
print(next(z_iter))#2
print(next(z_iter))#3
print(next(z_iter))#4
print(type(z_iter))#<class 'range_iterator'>

