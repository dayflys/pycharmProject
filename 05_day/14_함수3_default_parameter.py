'''
    함수(function)
    1.여러개 값을 리턴할 수 있다. (착시효과로써 반드시 1개만 리턴 가능하다.)
    2.default 파라미터 사용


'''
#1. 함수 호출시 전달값과 함수의 변수의 갯수가 일치되어야 한다.
def fun():
    pass

fun()
#fun(10) #parameter의 갯수가 불일치해서 에러발생

#2. default 파라미터 사용 ==> 함수의 변수가 더 많은 경우
def fun2(n = 10):
    print("fun2",n)

#fun2()#default값이 없다면, 파라미터 값을 주지 않을 때 에러발생
fun2()#default값이 있다면, 에러 발생 안함

def fun3(n=10,n2=20):
    print('fun3',n,n2)

fun3()
fun3(100)
fun3(1,2)

def fun4(x,n=10,n2=20):
    print('fun4',x, n,n2)

# fun4() #default 값이 없는 x는 값을 무조건 넣어주어야 한다.
fun4(100)
fun4(1,2)