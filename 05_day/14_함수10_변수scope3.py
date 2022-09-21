'''
    nonlocal 및 global 키워드

    1. 모든 함수는 중첩이 가능하다.
    2. 중첩된 함수는(mbc함수)는 global 영역에서 직접 호출 불가능하다.
        global 함수(kbs 함수)에서 중첩함수(mbc) 호출 한다.

'''
#1. 모든 변수 명이 다른 경우
n = 10 #전역 변수(global 변수)
def kbs():
    n2 = 20 #지역 변수(local 변수)
    print('kbs:',n,n2)
    def mbc():
        n3 = 30 #지역 변수(local 변수)
        print("mbc: ",n,n2,n3)
    mbc()
kbs()
print(n)
#print(n2) #에러발생-> 지역 변수기 때문에 함수 안에서만 쓸 수 있다
#print(n3) #에러발생-> 지역 변수기 때문에 함수 안에서만 쓸 수 있다.

#2. 모든 변수명을 동일하게 지정
n = 10 #전역 변수(global 변수)
def kbs():
    n = 20 #지역 변수(local 변수)
    print('kbs2:',n)#kbs: 20
    def mbc():
        n = 30 #지역 변수(local 변수)
        print("mbc2:",n) #mbc: 30
    mbc()
kbs()
print(n)#10

#3. 변수명이 겹치는 경우
n = 10 #전역 변수(global 변수)
def kbs():
    n = 20 #지역 변수(local 변수)
    print('kbs3:',n)#kbs: 20
    def mbc():
        print("mbc3:",n) #mbc: 20
    mbc()
kbs()
print(n)#10

#4. 변수명이 겹치는 경우
n = 10 #전역 변수(global 변수)
def kbs():
    n = 20 #지역 변수(local 변수)
    print('kbs4:',n)#kbs4: 20
    def mbc():
        # n = 30 #해결 1
        # nonlocal n#해결 2 nonlocal -> 이 함수블럭의 지역 변수가 아닌 가장 가까운 동일 변수수 나타내는 코드
        global n#해결 3 global -> 동일 이름의 전역변수를 일컫는다는 표현
        print("mbc4:",n)#mbc4: 20
        n = 30 #UnboundLocalError: local variable 'n' referenced before assignment
    mbc()
kbs()
print(n)#10