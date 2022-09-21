'''
    함수(function)
    1.여러개 값을 리턴할 수 있다. (착시효과로써 반드시 1개만 리턴 가능하다.)
    ===> 집합형에 먼저 저장하고 나중에 집합형을 리턴한다.

    2.return 키워드 2가지 용도(자바도 동일)
        가. 리턴값을 반환하기 위해서(주목적)
        나. 함수를 중지 목적
        (반복문을 중지하는 방법은 break)

'''
#1.여러개 값을 리턴할 수 있다.
def fun():
    return 10,20

result = fun()
print(result) #(10,20) => 여러개 값을 리턴하는 것이 아니라, 튜플로 리턴한다.

#2.return 키워드 2가지 용도(자바도 동일)
#함수를 중지 목적
def fun2():
    print("fun2")
    if True: return
    print("fun2-1")
    print("fun2-2")
fun2()
print("end")