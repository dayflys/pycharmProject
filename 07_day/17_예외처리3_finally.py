'''

    예외 처리
    - finally - 예외의 발생 유무와 상관없이 실행되는 문장

    문법:
        try:
            문장
        except 예외 클래스 [as 별칭]:
            문장
        -> 예외 처리 목적

        try:
            문장
        finally:
            문장
        => 반드시 수행 문장을 알려주는 것

        try:
            문장
        except 예외 클래스 as 별칭:
            문장
        finally:
            문장 -> 예외 발생여부와 상관없이 무조건 수행
        => 예외 처리 목적 + 반드시 수행 문장

        (자바는 try~catch~finally)



'''

try:
    n = 0
    result = 50 / n
    print('result', result)
except ZeroDivisionError as e:
    print("0으로 나누어서 예외가 발생",e)
finally:
    #파이썬에서 외부 자원(DB,파일등)을 사용할 때는 반드시 open 함수를 사용한다. 사용 후에는 close 함수를 사용한다. => 보통 close 함수를 finally 블럭에 작성한다.
    print("예외발생여부와 상관없이 무조건 수행")


try:
    print(999)
finally:
    print('success')

try:
    print(000)
except ArithmeticError as e:
    print("예외 발생시")
else:#예외가 발생하지 않을 때 실행하는 문장이다.
    print("예외가 발생이 안 됐을 때")