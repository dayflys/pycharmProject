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
n = 10 # 전역 변수 (global 변수)
# def fun():
#     x = 100
#     print('fun',x,n) #fun 100 10
# fun()
# print(x) #지역 변수를 전역으로 사용하려 해서 에러 발생

if True:
    x = 100 #전역 변수
    print(n,x)
print(">>>>",x)#>>>> 100 -> x를 쓸수 있다. 그 이유는 파이썬은 함수 내에 있는 변수만을 지역변수 취급하기 때문에
# if, for ,while 문 등 안에서 선언된 변수들은 전역 변수 취급한다.

for k in 'hello':
    x2 = 200
    print(x2)
print('>>>',x2)#>>> 200

