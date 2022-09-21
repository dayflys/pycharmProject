'''
    generator 함수
    -> 함수 블럭 안에 있는 문장을 전부 실행하는 것이 아니고,
    -> 함수 내의 yield 단위 기준으로 끊어서 실행 해준다.

    1. 함수 안에, yield 키워드로 실행할 코드를 묶어 준다.
    2. 일반적인 함수호출하면 실행이 되고 끝이지만, generator 함수 호출하면 반환 값인 generator 객체를 반환한다.
    => generator객체의 next() 함수 호출해서 yield 단위로 실행 할 수 있다.
'''
#일반 함수
def fun():
    print('111')
    print('222')
    print('333')

fun() #111 222 333

#generator 함수
def fun2():
    n = 10
    print('>>>>>111')
    yield
    print(n)
    print('>>>>>222')
    yield
    print('>>>>>>333')
    yield
gen = fun2()
print(gen) #<generator object fun2 at 0x1051c1f50>
next(gen)#>>>>>111
next(gen)#10 >>>>>222
next(gen)#>>>>>>333

#다. generator 함수 2 - yield 값
def fun3():
    n = 10
    print('>>>>>111')
    yield 100
    print(n)
    n=20
    print(n)
    print('>>>>>222')
    yield 200
    print(n)
    print('>>>>>>333')
    yield 300
gen = fun3()
result = next(gen)
result1 = next(gen)
result2 = next(gen)
print(result)
print(result1)
print(result2)