'''
    포멧 출력

    예> 이름: 홍길동, 나이:20, 주소: 서울
        이름: 이순신, 나이:30, 주소:부산
    문법
    1.변수 ="이름:{} 나이: {} 주소: {} ".format('홍길동',20,'서울')
    주의할점
    --> 중괄호의 개수와 값의 개수가 같아야 한다.

    #위치 지정, 여러번 지정가능
    2. 변수= '이름: {} 나이:{} 주소:{}'.format('홍길동',20,'서울')
    ex) --> 여러번 지정한 예시
    mesg2 = '이름: {2},{2},{2} 나이:{1} 주소:{0}'.format('홍길동', 20, '서울')

    *key=value 형식(매우 중요)
    3.변수 ="이름: {name} 나이:{age}  주소:{address}  ".format(name='홍길동',age = 20, address='서울')

    4. 혼합 가능 (매우 중요)
    mesg4 ="이름: {0} 나이:{1}  주소:{address}  ".format('홍길동',20, address='서울')
'''
mesg='이름:{}, 나이:{}, 주소:{}'.format('홍길동',20,'서울')
print(mesg)

mesg2 = '이름: {2} 나이:{1} 주소:{0}'.format('홍길동', 20, '서울')
print(mesg2)
mesg3 = '이름: {2},{2},{2} 나이:{1} 주소:{0}'.format('홍길동', 20, '서울')
print(mesg3)

mesg4 ="이름: {name} 나이:{age}  주소:{address}  ".format(name='홍길동',age = 20, address='서울')
print(mesg4)

mesg5 ="이름: {0} 나이:{1}  주소:{address}  ".format('홍길동',20, address='서울')
print(mesg5)

# help("FORMATTING")
#--> format 함수에 대한 document를 확인할 수 있다.