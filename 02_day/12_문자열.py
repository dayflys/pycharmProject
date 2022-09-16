'''
    문자열
    -표현: '', "", """ """, ''' '''
    -타입: str => type("hello") -> <class 'str'>
                                => 문자열은 클래스(class)로 만들어짐.
                                    클래스의 구성요소(변수, 함수)
    -특징: immutable(값 변경 불가)
    -> s.count(sub[, start[, end]])
    => mouseover 했을 시
        =>def count(self, x: str,__start: SupportsIndex | None = ...,__end: SupportsIndex | None = ...)
        =>def count(x:문자열, __start:타입=임의의 기본값,__end:타입=임의의 기본값) <- 윗 줄 해석본
'''

# print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  #여기서 부터 함
#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
#  'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
#  'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
#  'join', 'ljust', 'lower', 'lstrip',// 'maketrans', 'partition', 'removeprefix', 'removesuffix',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
#  'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

s = 'sAqUeNcE'
s_1 = 'tab'
s_tabs = 'sequ\tence'
s_dict = {'value': True}

print('1.문자열 길이: ',len(s)) # 1.문자열 길이:  8 => len은 builtins의 함수 이다.
print('2. 첫 글자 대문자: ', s.capitalize()) # 2. 첫 글자 대문자:  Sequence
print('3. 특정 문자의 개수: ', s.count('e')) # 3. 특정 문자의 개수: 1
print('4. 대문자: ', s.capitalize()) # 4. 첫글자만 대문자 나머지 소문자: Saquence
print('5. 소문자: ', s.lower()) # 5. 소문자: saquence
print('6. swapcase(대<->소): ', s.swapcase()) # 6. 대소문자 swap: SaQuEnCe
print('7.공백제거','     hello     '.strip(),len('     hello     '.strip())) #7.양쪽 공백 제거 hello 5
print('8.왼쪽공백제거','     hello     '.lstrip(),len('     hello     '.lstrip())) #8.왼쪽 공백 제거 hello 10
print('9.오른쪽공백제거','     hello     '.rstrip(),len('     hello     '.rstrip())) #9.오른쪽 공백 제거 hello 10
print('10.특정문자제거','HHHhelloHHH'.strip("H"),len('HHHhelloHHH'.strip("H"))) #10.특정문자 제거 hello 5
print('11.왼쪽특정문자제거','HHHhelloHHH'.lstrip("H"),len('HHHhelloHHH'.lstrip("H"))) #11.왼쪽 특정문자 제거 HHHhello 8
print('12.오른쪽특정문자제거','HHHhelloHHH'.rstrip("H"),len('HHHhelloHHH'.rstrip("H"))) #12.오른쪽 특정문자 제거 HHHhello 8
print('13.값 치환','HelHloH'.replace("H", "A")) #13. 값 치환 AelAloA
print('14.값 치환, count 수 제한','HelHloH'.replace("H", "A",1)) #14. 값 치환, count 수 제한 AelHloH
print('15.특정문자로 시작여부','HelHloH'.startswith("H")) #15. 특정 문자로 시작여부 True
print('16.특정문자로 끝나는 여부','HelHloH'.endswith("H")) #16. 특정 문자로 끝나는 여부 True
print('17.특정문자로 분리','AAA/BBB/CCC'.split("/"))#17. 특정문자로 분리=> 리스트로 저장 ['AAA', 'BBB', 'CCC']
a,b,c = 'AAA/BBB/CCC'.split("/")
print(a,b,c)
print('18.특정문자의 위치값 반환:','HelHloH'.find("e")) #18.특정문자의 위치값 반환: 1
print('19.특정문자의 위치값 반환(실패):','HelHloH'.find("x")) #19.특정문자의 위치값 반환: 실패 시 -1
print('20.오른쪽 패딩처리:','HelHloH'.ljust(10,"*")) #20.오른쪽 패딩 처리: HelHloH*** 문자는 하나만 가능
print('21.왼쪽 패딩 처리:','HelHloH'.rjust(10,"*")) #21.왼쪽 패딩 처리: ***HelHloH
print('22.양쪽 패딩 처리:','HelHloH'.center(10,"*")) #22.양쪽 패딩 처리: *HelHloH**
print('23.join:','.'.join(['ab','pq','rs'])) #23.문자로만 구성됐냐?: ab.pq.rs
print('24.문자로만 구성됐냐?:','HelHloH홍길동'.isalpha()) #23.문자로만 구성됐냐?: True
print('25.숫자로만 구성됐냐?:','124HH'.isnumeric()) #23.숫자로만 구성됐냐?: False
print('26.숫자로만 구성됐냐?:','124'.isnumeric()) #23.숫자로만 구성됐냐?: True

#집합형에 저장된 문자열을 join에 설정된 값으로 연결, => interable : 반복할 수 있는, 집합형




print('1.문자열 길이: ',len(s)) # 1.문자열 길이:  8 => len은 builtins의 함수 이다.
print('2. 첫 글자 대문자: ', s.capitalize()) # 2. 첫 글자 대문자:  Sequence
print('3. 모든 글자 소문자: ', s.casefold())
# 3. 모든 글자 소문자(대소문자가 없는 경우, 영어와 대응되는 값있으면 그걸로 출력):  Sequence
print('4. 특정 문자의 개수: ', s.count('e')) # 4. 특정 문자의 개수: 3
print('5. 지정 인코딩 방식을 사용해 문자열 변(미지정 경우 utc-8): ', s.encode()) # 4. 지정 인코딩 방식을 사용해 문자열 변(미지정 경우 utc-8): b'sequence'
print('6. 가운데 정렬: ', s.center(10,'*')) # 5.가운데 정렬 : *sequence*
print('7. 특정 문자로 끝나는 지: ', s.endswith('e')) # 6. 특정 문자로 끝나는 지: True
print('8. tab의 크기를 지정: ', s_tabs.expandtabs(4)) # 7. tab의 크기를 지정:  sequ    ence
print('9. 특정 문자가 처음으로 나오는 index: ', s.find('e')) # 8. 특정 문자가 처음으로 나오는 index: 1
print('10. format(딕셔너리) 역할을 진행 : {value} '.format_map(s_dict)) # 10. format(딕셔너리) 역할을 진행 : True
print('11. 특정 문자의 index : ',s.index('s')) # 11. 특정 문자의 index : True
print('12. 알파벳이나 숫자인지 판별 : ',s.isalnum()) # 12. 알파벳이나 숫자인지 판별 : True
print('13. 알파벳인지 판별 : ',s.isalpha()) # 13. 알파벳인지 판별 : True
print('14. string이 아스키코드인지 판별 : ',s.isascii()) # 14. 아스키코드인지 판별 : True
print('15. 10진법인지 판별 : ',s.isdecimal()) # 15. 십진법인지 판별 : False
print('16. 숫자인지 판별 : ',s.isdigit()) # 16. 숫자인지 판별 : False
print('17. 식별자인지 판별 : ',s.isidentifier()) # 17. 식별자(사용자 지정도 포함)인지 판별 : True
print('18. 소문자인지 판별 : ',s.islower()) # 18. 소문자인지 판별 : True
print('19. 숫자인지(적어도 한개) 판별 : ',s.isnumeric()) # 19. 숫자인지(적어도 한개) 판별 : False
print('20. 출력할 수 있는지 판별 : ',s.isprintable()) # 20. 출력할 수 있는지 판별 : True
print('21. 공백이 있는지 판별 : ',s.isspace()) # 21.공백이 있는지 판별 : False
print('22. 대문자인지 판별 : ',s.isupper()) # 22.대문자인지 판별 : False
print('23. s_1 사이사이에 문자열 출력: ',s.join(s_1)) # 23. s_1 사이사이에 문자열 출력 : tsequenceasequenceb
print('24. 숫자크기만큼 오른쪽에 채우기 : ',s.ljust(10,'1')) # 24. 숫자크기만큼 오른쪽에 채우기 : sequence11
print('25. 소문자로 바꿔줌 : ',s.lower()) # 25. 소문자로 바꿔줌 : sequence
print('26. 왼 쪽 공백 제거: ',s.lstrip()) # 26. 왼 쪽 공백 제거: sequence



