'''
    일급 객체(first-class)
    ===> 파이썬, 자바스크립
    개요:
    -함수를 데이터로 처리한다.
    -데이터를 사용할 수 있는 위치면 전부 사용이 가능하다.

    1) 함수를 변수에 저장할 수 있다.
        예> 변수 = 10
            변수 = '홍길동'
            변수 = [10,20,30]

            변수 = 함수

    2) 함수를 다른 함수 호출시 인지 값으로 쓸 수 있다.
    예>
        fun(10)
        fun("홍길동")
        fun([10,20])

        fun(함수)

    3) 함수 실행 후 리턴 값으로 함수를 사용할 수 있다.
    예>
        return 100
        return '홍길동'
        return [10,20]

        return 함수

    4. 함수가 메모리에 올라가는 과정
    -> 1. 함수명으로된 변수가 생성
    -> 2. 함수 자체 객체가 생성
    -> 3. 함수명이 함수 객체를 참조
    -> * 다른 변수들도 참조를 할 수 있다.
    -> 따라서 이러한 방법으로도 함수를 호출 할 수 있다.
    =>
    def fun():
        print("fun")

    x= fun
    x()

'''
#1.함수를 변수에 저장할 수 있다.
def fun():
    print("fun")

xx = fun
xx()#fun
#2. 함수를 다른 함수호출 시 인자값(argument)으로 사용 가능하다.
#트리거(trigger) 함수로서 구현 방법은 함수호출 시 인자값으로 호출할 함수명을 전달해주면 된다.
def fun1():
    print("fun1")

def fun2():
    print("fun2")

def fun3(f):
    f()

fun3(fun2)#fun2
fun3(fun1)#fun1

#함수 실행 후 리턴 값으로 함수를 사용할 수 있다.

def m():
    print('m')

def m2():
    return m #함수를 리턴

xx = m2()
xx()#m