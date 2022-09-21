'''

    파이썬 반복문
    1.for문 while문 (do~while문 제공 안됨)

    2.while문 문법:

        변수 = 초기값
        while 조건식:
            문장
            변수증가코드(증감식)
    ===> 조건식에 따라서 무한루프 또는 실행이 아예 안 될 수 있다.

    ===> 일정 횟수 반복 용도
    ===> for 문은 반복회수 예측이 가능할 때.
        while문은 예측이 힘들 때 주로 사용이 된다.


'''
n = 1
while n <= 5:
    print('hello', end=' ')#hello hello hello hello hello
    n += 1
