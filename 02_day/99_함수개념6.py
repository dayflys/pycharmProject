'''
    함수의 기본 개념
'''
#1. 함수 호출 시 반드시 parameter와 input의 개수가 일치해야 한다.
def fun():
    pass

fun()
#fun(10)

#2. 기본값 지정하면 불일치 가능
def fun2(n,n2=10):
    pass

fun2(10)
fun2(10,20)

#3. packing 지정하면 불일치 가능, 다만 마지막 인자에만 적용 가능 => 튜플로 출력됨
def fun3(n,n2,*n3):
    print(n,n2,n3)
    pass
fun3(1,2,3,4,5,6)#1 2 (3, 4, 5, 6)

#4. dict packing 지정하면 불일치 가능, 다만 마지막 인자에만 적용 가능 => dict로 출력됨
def fun4(**n3):
    print(n3)
    pass
fun4(name="홍길동",age=20)#{'name': '홍길동', 'age': 20}


#5. 3,4 둘다 사용 가능
def fun5(*x,**y):
    print(x,y)
    pass
fun5(1,2,3,4,5,6,name="홍길동",age=20)#(1, 2, 3, 4, 5, 6) {'name': '홍길동', 'age': 20}