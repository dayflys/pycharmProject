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

    * 무한루프

        while True:
            if 조건: break
            문장

        문장

'''

while True:
    print("메뉴")
    print("------------------------")
    print("1. 게시판 목록 보기")
    print("2. 게시판 글 저장하기")
    print("0. 종료하기")
    s = input("번호 입력")
    if s == '1':
        print('게시판 목록 완료')
    elif s == '2':
        print('글 저장 완료')
    elif s == '0': break
    else: print('유효한 숫자를 입력하세요')
print('프로그램 정상 종료')

