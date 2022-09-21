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

#2. 변수명이 겹치는 경우
