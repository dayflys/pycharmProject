'''

    람다(lambda) 함수
    -def 함수의 다른 표현 방법 => but, 단일 표현식인 경우만 가능.
    -> 즉 함수 표현식에서 body 블록에 한 문장만 있는 경우만 가능

    람다 표현식(lambda)
    개요:
        def 함수의 또 다른 표현식

    특징:
    -반드시 단 하나의 실행문을 가진 경우만 람다 표현식으로 변경할 수 있다,
    -함수명이 없다. => 익명함수,anonymous function
    -> 명시적으로 변수에 저장해서 사용한다. (일급객체 특징)
    문법:

        변수명 = lambda [변수,변수2,....]: 문장
'''
#1.파라미터가 없고 리턴 값이 없는 형태

def fun():
    print('fun')

fun2 = lambda : print('lambda fun')

fun() #fun
fun2() #lambda fun

#2.파라미터가 있고 리턴값이 없는 형태
def fun(n,n2):
    print('fun',n,n2)

fun2 = lambda n,n2: print('lambda fun',n,n2)

fun(10,20) #fun 10 20
fun2(10,20) #lambda fun 10 20

#3. 파라미터 없고 리턴 값이 있는 형태
def fun():
    return 100

fun2 = lambda : 100 #람다 함수에서는 리턴이 있는 문장에서는 값만 작성

print(fun()) #100
print(fun2()) #100

#3. 파라미터 있고 리턴 값이 있는 형태

def fun(n,n2):
    return n+n2

fun2 = lambda n,n2: n+n2 #람다 함수에서는 리턴이 있는 문장에서는 값만 작성

print(fun(10,20)) #30
print(fun2(10,20)) #30
