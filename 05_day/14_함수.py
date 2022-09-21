'''
    함수(function)
    1. 용도
     -기능 처리 담당 (데이터(값) 저장 담당: 변수)

    2.특징
     - 반드시 호출 해야 수행 되고, 수행 후 에는 호출된 곳으로 되돌아 간다.
     -함수 호출 시 함수쪽으로 임의의 값(전달값,파라미터,parameter)을 전달할 수 있다.
     -전달값이 있으면 함수쪽에서는 전달 값을 저장하기 위해서 변수가 필요하다.
     -전달 값의 개수는 여러개가 가능하다.
     -기본적으로 전달 값과 함수쪽의 변수의 갯수는 반드시 일치해야 한다.

     -호출 후 함수가 실행되고, 호출한 곳으로 돌아올 때 임의의 값(리턴값)을 가지고 반환될 수 있다.
     -호출 한 곳에서는 리턴 값을 저장하기 위해서 변수가 필요하다.
     -리턴값의 갯수는 반드시 1개다.(리턴값이 여러개가 될 수 없다.여러개 처럼 보인다.)

    3. 문법

        가. 파라미터가 없고 리턴 값도 없는 경우
        나. 파라미터가 있고 리턴 값이 없는 경우
        다. 파라미터가 없고 리턴 값이 없는 경우
        라. 파라미터가 있고 리턴 값이 있는 경우

    def 함수명([변수1,변수2,...]): #변수 용도는 전달 값(파라미터) 저장용.
        문장
        문장
        ..
        [return 값] #값을 '리턴값'이라고 한다.

    호출방법:
    -> 함수명([값,값2,...])
'''

#가. 파라미터가 없고 리턴 값도 없는 경우
def fun():
    print('fun')
fun()#fun

#나. 파라미터가 있고 리턴 값이 없는 경우
def fun2(n):
    print('fun2 ',n)
fun2(10)#fun2  10
fun2('홍길동')#fun2  홍길동
fun2([1,3,4])#fun2  [1, 3, 4]

def fun3(n,n2):
    print('fun3 ',n,n2)
print(10,20)#10 20
print(10,'홍')#10 홍
print('박','홍')#박 홍
print([1,2,3],'홍')#[1, 2, 3] 홍

#다. 파라미터가 없고 리턴 값이 없는 경우
def fun4():
    # return 100
    # return '홍'
    return [1,2,3]
n = fun4()
print(n)#[1, 2, 3]


def keyboard_input():
    s = input("번호 입력")
    return s

def menu_print():
    print("메뉴")
    print("------------------------")
    print("1. 게시판 목록 보기")
    print("2. 게시판 글 저장하기")
    print("0. 종료하기")


"""while True:
    menu_print()
    s = keyboard_input()
    if s == '1':
        print('게시판 목록 완료')
    elif s == '2':
        print('글 저장 완료')
    elif s == '0': break
    else: print('유효한 숫자를 입력하세요')
print('프로그램 정상 종료')"""

#라. 파라미터가 있고 리턴 값이 있는 경우
def fun5(n,n2):
    result = n+n2
    return result

n = fun5(10,20)
print(n)#30

# 실습 문제: 두개의 정수값을 받아서 큰값을 반환하는 함수
def max_select(n,n2):
    if n > n2:
        return n
    else:
        return n2
print(max_select(10,20)) #20

def max_select(n,n2):
    result = [n,n2]
    result.sort()
    return result[-1]
print(max_select(10,20))#20

def max_select(n,n2):
    result = n2
    if n > n2:
        result= n
    return result
print(max_select(10,20))#20

#문제2: 임이의 문자열을 입력 받고 5글자 이상으로 된 문자열은 '5글자...' 포맷을 반환하는 함수를 작성하시오
def literal(a):
    if len(a) > 5:
        return a[:5]+'...'
    else:
        return a
print(literal("helloworld!"))#hello...

#문제3: 주민번호 목록(리스트 목록)을 입력받고 여성(남성)만 리스트로 반환하는 함수를 작성하시오

def gender_select(x):
    result = []
    for i in range(len(x)):
        if x[i][7] == '1':
            result.append('M')
        else:
            result.append("F")
    return result

data=['891202-1234125','960523-1234125','201202-1234125','791202-2234125','211202-2234125']
data_result = gender_select(data)
print(data_result)#['M', 'M', 'M', 'F', 'F']

def ssn_security(x):
    result = [i[:8]+'*'*6 for i in x]
    return result
data=['891202-1234125','960523-1234125','201202-1234125','791202-2234125','211202-2234125']
data_result = ssn_security(data)
print(data_result)#['891202-1******', '960523-1******', '201202-1******', '791202-2******', '211202-2******']