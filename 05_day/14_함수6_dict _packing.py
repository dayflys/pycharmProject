'''
    함수(function) ~= 메서드(method)
    용도: 기능 처리
    특징:
    -반드시 호출해야 함수가 실행이 된다.
    -실행이 끝나면, 호출한 곳으로 돌아온다.
    -호출 시, 값을 전달이 가능하다. 여러개 전달 가능
    -함수 쪽에서는 전달할 값을 저장할 변수가 필요하다.
    -실행 후에는 호출한 곳으로 값을 가지고 돌아올 수 있다.(리턴 값)
    ------------------여기까지는 모든 언어의 함수의 특징
    -default 파라미터
    -변수가 더 많을때 packing(*)
    -값이 더 많을 때 named parameter

    python 함수 문법
    def 함수명([변수,변수2, ...]):
        문장
        [return 값]

    *parameter - 파라미터 -> 함수 작성시 들어가는 변수값
    argument - 인자값 -> 함수 호출 시 들어가는 인자값

        6. dict packing
    ====> named 파라미터로 전달한 여러 인자값(argument)을
        함수 쪽에서 dict로 저장할 수 있는 방법
'''

#혼합 가능
def func3(name,age,address):
    print(name,age,address)

func3('홍길동',20,'서울')#홍길동 20 서울
func3(name='홍길동',age=20,address='서울')#홍길동 20 서울
func3('홍길동', address='서울',age=20)#홍길동 20 서울

#dict packing
def fun(**k):
    print(k)

fun(x=100, y=200)#{'x': 100, 'y': 200}
fun(y2=100, x2=200)#{'y2': 100, 'x2': 200}
fun(a=100, b=200,c=300)#{'a': 100, 'b': 200, 'c': 300}

#3가지 혼합 가능
def fun2(n,n2,*n3,**n4):#순서중요
    print(n,n2,n3,n4)

fun2(10,20,'홍길동','이순신',name='유관순', age=20)#10 20 ('홍길동', '이순신') {'name': '유관순', 'age': 20}
