'''
    예외 처리

    #OOP의 3대 특징
    1. 상속
    2. 다형성 (polymorphism)
    3. 은닉화(encapsulation)
'''

print("1>")

try:
    n = 0
    result = 50 / n
    print('result', result)#예외가 발생되면 바로 except 문장으로 넘어가기때문에 이 문장이 실행되지 않음

except BaseException as e:#적합한 예외 클래스를 써야 except가 적용된다. 다만 부모 클래스는 사용 가능하다. 따라서 Exception과 BaseException도 가능하다
    #BaseException as e가 e=BaseException() 동일
    #참조변수를 print(e) gkaus __str__(self) 호출된다.
    #division by zero 문자열이 출력되었기 때문에
    #__str__(self)가 리턴하는 값은 division by zero라고 추측할 수 있다.
    #재정의 했음
    print("0으로 나누어서 예외가 발생", e)#예외가 발생되지 않으면 실행이 안된다. 최선의 예외 처리는 친절히 정보를 알려주는 것임


print("end 정상종료 ")