'''

    변수 scope
    1) 개념
        선언된 변수 사용 가능한 범위(scope,context)를 의미한다.
    2) python의 변수 scope
    ===> 함수 scope를 따른다.
        즉, 함수 내에서 선언된 변수는 함수 안에서만 사용 가능하다.

    3) 변수의 종류

        가. 전역 변수(global variable)
        => 함수 밖에서 선언된 함수

        나. 지역 변수(local variable)
        => 함수 안에서 선언된 함수
'''
n = 10 # 전역변수 (global 변수)
def fun():
    x = 100
    print('fun',x,n) #fun 100 10
fun()
# print(x) #지역변수를 전역으로 사용하려 해서 에러 발생
