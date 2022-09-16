'''

    비교연산자
    1. A > B
    2. A < B
    3. A == B
    4. A <= B
    5. A >= B
    6. A != B
    -> A를 기준으로 판단하며, 출력값은 논리값(True, False)로 나온다.

    비교 연산자
    -같냐? ( == 연산자 사용 )
    -같지 않냐? ( != 연산자 사용)

    - 실행 결과는 논리값(True, False)

'''

n = 10
n2 = 9

print(n==n2)#False
print(n!=n2)#True
print(n<n2)#False
print(n>n2)#True
print(n<=n2)#False
print(n>=n2)#True

#문자열도 상관 없다.

m = 'aaa'
n = 'bbb'
print(m == 'aaa')#True
print(m>n)#False
print(m<n)#True


#None 비교
x = None
print(x == None)#True -> == None 으로 비교 할 수 도 있고
print(x is None)#True -> is None 으로 비교 할 수 도 있다. -> 그래도 이 걸 권장

#print( x== None)
print(x is None)#True 권장
print(x is not None)#False 권장