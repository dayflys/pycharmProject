'''
    포멧 출력

    1.''.format(값) 방식 ==> 권장

    2. 이전 방식 -> data type에 따른 표현식을 사용한다. 값에 맞는 데이터 타입에 순서대로 들어간다.
    "이름:%s  나이:%d 키:%f 성별:%c "%(값, 값2, 값3, 값4)
    "이름:%s  나이:%d 키:%.2f 성별:%c "%('홍길동', 20, 177.424, "남")
    %s: 문자열
    %d: 정수
    %f: 실수
    %c: 문자 하나
    등등 있다.

    3. 정렬 (공백|공백 채울 문자 <|^|> 자리수)
    < => 왼쪽 정렬
    ^ => 가운데 정렬
    > => 오른쪽 정렬

    4.format string
    => f""
    => 장점: "" 안에 변수 이름 사용 가능
    => 장점2: {}안에서 연산도 가능하다. 산술 연산, 비교 연산 등
    => 장점3: {}안에서 함수 호출도 가능하다
'''


name = "Shiro"# 문자열 ==> str==> str의 함수 <- print(dir(str))로 확인한 것
age = 20
mesg = f"이름:{name.upper()} 나이:{age}"
print(mesg)