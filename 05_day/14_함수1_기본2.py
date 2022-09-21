'''
    함수 정의시 리턴 값 타입 명시 가능
    def 함수명()-> 리턴타입:
        pass
        return 'hello'

'''

def fun()-> str:
    return 'hello'
print(fun())
def fun2()-> None:
    return 100

#리턴 값과 명시된 타입이 일치하지 않아도 문법적으로 문제가 없다.

def fun3()-> int:
    return "100"