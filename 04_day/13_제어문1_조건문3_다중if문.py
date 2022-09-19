"""
    문장(statement)
    -실행문
        -> 순차문:위에서 아래로 순차적으로 실행되는 문장
            -> 한번 실행된 문장은 재실행 불가
        -> 제어문 => 들여쓰기 주의
            -> 조건문(분기문)
                => 단일 if문
                => if else 문
                => 다중 if 문
            -> 반복문(여러번 시행 될 수 있다) -특정한 범위에 있는(블럭안에 있는) 실행 문을 반복적으로 시행한다.
                => for문
                => while 문
    
    -비실행문:주석문
    -> 한줄 주석은 #로
    -> 여러줄 주석은 ''' ''' 이나 """ """로 작성
            
    제어문
    1.단일 if문 ==> 조건이 참인 경우에만 실행시키는 문장 지정 가능
        문장1
        #명시적인 True/False 가 아니고 논리값이 나올 수 있는 연산자를 주로 사용하는 것이 일반적이다.
        #비교연산자, 논리연산자, 멤버십 연산자(in 연산자), is None, isinstance()등등 
        # 또는 일반데이터 또한 논리값으로 활용이 가능하기 때문에 이를 이용해서 조건식을 활용할 수 있다
        # 또는 일반 데이터(일반형, 집합형)을 논리값으로 변경하는 함수
        if 조건식:
            문장2
            문장3
        문장4
    
    2. if~else문
    
    문장1
    if 조건식: -> if 블럭
        문장2
    else: -> else 블럭
        문장3
    문장4
    
    3. 다중 if문
    ==> 여러번 비교해야 되는 경우에 사용됨
    if 조건식1: -> if 블럭
        문장2
    elif 조건식2: -> elif 블럭
        문장3
    elif 조건식3: -> elif 블럭
        문장4
    else: 
        문장5
    문장6
    
"""

num = 3
s = 'hello'
s2 = []
print('1')
# if True:
# if num > 4:
# if num > 4 or num == 3:
# if 10 in [10,20,30]:
# if isinstance(10,int):
# if bool(num):
# if num:
# if s:
# if [10]: #리스트에 값이 존재하냐?
if 'hello':
    print('2')
    print('2-1')
    print('2-2')
print('3')
print('4, end')

#만약에 영향 받는 문장이 하나라면 한줄로 사용할 수 있다.
if True: print("True")

#키보드로 값을 입력 받아서 짝수인지 홀수 인지 출력

num = int(input("숫자를 입력하세요: \n"))
if num%2 == 0:
    print("짝수")
else:
    print("홀수")
print('end')

num = int(input("점수를 입력하시오 : \n"))

if num >= 90:
    print("A")
elif num >= 90:
    print("B")
elif num >= 90:
    print("C")
else:
    print("D")
