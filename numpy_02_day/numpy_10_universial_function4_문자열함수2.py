'''

    범용 함수 (universial function)

    1. 개념
        데이터의 요소별로 연산을 수행하는 함수 => 이로인해 벡터 연산이 가능하게 한다.

    문자열 함수 => np.char.함수 로 이용한다.

    문자열 관련 범용 함수

    1. 문법

        np.char.함수명

'''

import numpy as np

npc = np.char

#1. np.char.add() => 문자열 연결
x = np.array(["AAA","BBB"])
x2 = np.array(["AAA2","BBB2"])
print("1. 문자열 연결: ", npc.add(x,x2)) #1. 문자열 연결:  ['AAAAAA2' 'BBBBBB2']

#2. np.char.multiply() => 지정된 개수 만큼 문자열 연결
x = np.array(["AAA","BBB"])
print("2. 문자열 연결: ", npc.multiply(x,2)) #2. 문자열 연결:  ['AAAAAA' 'BBBBBB']

#3. np.char.capitalized() => 첫 글자 대문자
x = np.array(["hello world","say good bye", 'who are you'])
print("3. 첫 글자 대문자: ", npc.capitalize(x)) #3. 첫 글자 대문자:  ['Hello world' 'Say good bye' 'Who are you']

#4. np.char.upper() => 모두 대문자
x = np.array(["hello world","say good bye", 'who are you'])
print("4. 모두 대문자: ", npc.upper(x)) #4. 모두 대문자:  ['HELLO WORLD' 'SAY GOOD BYE' 'WHO ARE YOU']

#4. np.char.lower() => 모두 소문자
x = np.array(["hello world","say good bye", 'who are you'])
print("5. 모두 소문자: ", npc.lower(x)) #5. 모두 소문자:  ['hello world' 'say good bye' 'who are you']

#6. np.char.swapcase() => swapcase
x = np.array(["hello world","say good bye", 'who are you'])
print("6. swapcase: ", npc.swapcase(x)) #6. swapcase:  ['HELLO WORLD' 'SAY GOOD BYE' 'WHO ARE YOU']


#7. np.char.title() => 단어별 첫글자 대문자
x = np.array(["hello world","say good bye", 'who are you'])
print("7. 단어별 첫글자 대문자: ", npc.title(x)) #7. 단어별 첫글자 대문자:  ['Hello World' 'Say Good Bye' 'Who Are You']

#8. np.char.rjust(),ljust(),center() => 정렬
x = np.array(["hello world","say good bye", 'who are you'])
print("8. 왼쪽 정렬: ", npc.ljust(x,20,fillchar="_")) #8. 왼쪽 정렬:  ['hello world_________' 'say good bye________' 'who are you_________']
print("8. 오른쪽 정렬: ", npc.rjust(x,20,fillchar="_")) #8. 오른쪽 정렬:  ['_________hello world' '________say good bye' '_________who are you']
print("8. 가운데 정렬: ", npc.center(x,20,fillchar="_")) #8. 가운데 정렬:  ['____hello world_____' '____say good bye____' '____who are you_____']

#9. np.char.rstrip(),lstrip(),strip() => 공백 제거
x = np.array(["     hello world       ","     say good bye      " , '     who are you       '])
print("9. 왼쪽 공백 제거: ", npc.lstrip(x)) #9. 왼쪽 공백 제거:  ['hello world       ' 'say good bye      ' 'who are you       ']
print("9. 오른쪽 공백 제거: ", npc.rstrip(x)) #9. 오른쪽 공백 제거:  ['     hello world' '     say good bye' '     who are you']
print("9. 양쪽 공백 제거: ", npc.strip(x)) #9. 양쪽 공백 제거:  ['hello world' 'say good bye' 'who are you']

#9. np.char.rstrip(),lstrip(),strip() => 특정 문자 제거
x = np.array(["HHHHHhello worldHHHH","HHHHsay good byeHHHH" , 'HHHHwho are youHHHHHH'])
print("10. 왼쪽 특정 문자 제거: ", npc.lstrip(x,'H')) #10. 왼쪽 특정 문자 제거:  ['hello worldHHHH' 'say good byeHHHH' 'who are youHHHHHH']
print("10. 오른쪽 특정 문자 제거: ", npc.rstrip(x,'H')) #10. 오른쪽 특정 문자 제거:  ['HHHHHhello world' 'HHHHsay good bye' 'HHHHwho are you']
print("10. 양쪽 특정 문자 제거: ", npc.strip(x,"H")) #10. 양쪽 특정 문자 제거:  ['hello world' 'say good bye' 'who are you']

#11. np.char.split() => 구분자 이용해서 문자열 분리
x = np.array(["hello world","say good bye", 'who are you'])
print("11. 구분자 이용해서 문자열 분리: ", npc.split(x)) # 기본은 공백 11. 구분자 이용해서 문자열 분리:  [list(['hello', 'world']) list(['say', 'good', 'bye']) list(['who', 'are', 'you'])]
x = np.array(["hello/world","say/good/bye", 'who/are/you'])
print("11. 구분자 이용해서 문자열 분리: ", npc.split(x,'/')) # 기본은 공백 11. 구분자 이용해서 문자열 분리:  [list(['hello', 'world']) list(['say', 'good', 'bye']) list(['who', 'are', 'you'])]

#12. np.char.replace() => 문자열 변경
x = np.array(["hello/world","say/good/bye", 'who/are/you'])
print("12. 문자열 변경: ", npc.replace(x,'/','*')) # 12. 문자열 변경:  ['hello*world' 'say*good*bye' 'who*are*you']

#13. np.char.find() => 특정 문자열 위치
x = np.array(["hello/world","say/good/bye", 'who/are/you'])
print("13. 특정 문자열 위치: ", npc.find(x,'/')) # 13. 특정 문자열 위치:  [5 3 3]

#14. np.char.count() => 특정 문자열 빈도수
x = np.array(["hello/world","say/good/bye", 'who/are/you'])
print("14. 특정 문자열 빈도수: ", npc.count(x,'/')) #14. 특정 문자열 빈도수:  [1 2 2]

#15. np.char.join() => 특정 문자열 병합
x = np.array(["hello/world","say/good/bye", 'who/are/you'])
print(','.join(['1','2','3']))
# print(','.join([1,2,3])) #에러 발생 => 이유는 리스트안에 문자열이 아니라서
print("15. 특정 문자열 병합: ", npc.join('/',x)) #15. 특정 문자열 병합:  ['h/e/l/l/o///w/o/r/l/d' 's/a/y///g/o/o/d///b/y/e' 'w/h/o///a/r/e///y/o/u']

x2= np.array([1,2,3])
print("15. 특정 문자열 병합:", npc.join(',',x2.astype(np.str_))) #15. 특정 문자열 병합: ['1' '2' '3']

#16. np.char.isdigit() => 숫자인지 판별 => boolean 값 출력
x = np.array(["heLlo","20","56",'5Helo'])
print("16. 숫자인지 판별: ", npc.isdigit(x)) #16. 숫자인지 판별:  [False  True  True False]
print("16. 숫자인지 판별: ", npc.isalpha(x)) #16. 숫자인지 판별:  [ True False False False]
print("16. 숫자인지 판별: ", npc.isupper(x)) #16. 숫자인지 판별:  [False False False False]
print("16. 숫자인지 판별: ", npc.islower(x)) #16. 숫자인지 판별:  [False False False False]
print("16. 숫자인지 판별: ", npc.isnumeric(x)) #16. 숫자인지 판별:  [False  True  True False]
print("16. 숫자인지 판별: ", npc.isalnum(x)) #16. 숫자인지 판별:  [ True  True  True  True]

#17. np.str.replace()

x = np.array(["hello world","say good bye", 'who are you'], dtype=np.str_)
print(np.str.replace("Hello","e","E")) #HEllo => DeprecationWarning 이전 버전 함수이므로 사용을 권장하지 않

