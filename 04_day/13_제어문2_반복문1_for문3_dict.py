'''
    제어문(반복문)

    1. for문

        for 변수 in 집합형: => 집합형 개수만큼 반복됨
            문장

        가. 일정 횟수 반복 용도
        ===> range() 함수 이용해서 개수를 만들어 준다. => builtins 객체

        나. 집합형 데이터를 조회용 반복
        ==> enumerate() 함수 이용해서 반복 횟수 값을 얻을 수 있다. => builtins 객체

        ==> dict 인 경우 처리
            -dict.keys()
            -dict.values()
            -dict.items()
    2. while 문

'''
num = {'name': '홍', 'age':20, 'address': "서울"}

# 1.key만 얻기
for k in num.keys():
    print(k, end=' ')
print()

# 2.value만 얻기
for v in num.values():
    print(v, end=' ')
print()


# 2.key/value 둘 다 얻기 (*********)
for k,v in num.items():
    print(k, v, end=' ')
print()

for x in range(2,10):
    for y in range(1,10):
        print('{} X {} = {}'.format(x, y, x*y))

'''
    name age address 
홍 20 서울 
name 홍 age 20 address 서울 
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
'''