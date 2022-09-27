'''

    파일 포멧 종류
    1. .txt 파일 읽기/ 쓰기
    2. .csv 파일 읽기/쓰기 (쉼표로 구분된 문자열 의미)
        예> 홍길동,20, 서울
            .json 파일 읽기/쓰기 (json: javascript object notation, 자바스크립트에서 사용하는 객체 표현식, 매우 범용적으로 사용됨)
            ===> 현재 사용중인 프로그램 언어의 공통 포멧
            ===> {'key': 'value','key': 'value','key': 'value',...} 형

    파일 읽기/쓰기
                    open('파일경로',mode)
                    mode:   'r' => 읽기
                            'w' => 쓰기 (덮어쓰기)
                            'a' => 추가하기 (append)
        파이썬 프로그램 ---------------------> 파일(txt, csv, json 등)

                    close()


'''

'''
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__'
, '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__'
, '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__'
, '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__'
, '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable'
, '_checkWritable', '_finalizing'
여기서 부터 함수
, 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush'
, 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable'
, 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate'
, 'writable', 'write', 'write_through', 'writelines']
'''
#1. 읽기

f = open('./resourse/무제.txt','r', encoding="utf-8")

print(f.readline())# 한 줄 씩 출력

f.close()

#2. with 문
'''
with문은 자동으로 close 해준다.
with open('파일 경로','mode', encoding="utf-8") as 별칭
print(f.readline())
'''
print("*"*150)
#3. f.readline() 모두 읽기 ==> 반복문 처리
with open('./resourse/무제.txt','r',encoding='utf-8') as f:
    while True:
        line= f.readline()
        if not line: break
        print(line)
print("*"*150)
#4. f.read()
with open('./resourse/무제.txt','r',encoding='utf-8') as f:
    xxx = f.read() #f.read([글자 개수]) => 문자열 타입으로 전부 읽어 온다. 다만 escape 문자는 가져오지 않는 것 같다.
    print(xxx)

#5. f.readlines() ==> 리스트로 반환
print("*"*150)
with open('./resourse/무제.txt','r',encoding='utf-8') as f:
    xxx = f.readlines() #f.readlines() =>리스트 타입으로 전부 읽어 온다.
    for line in xxx:
        print(line)

#6. 파일이 없을 때 예외가 발생됨 ===> FileNotFoundError
try:
    with open('./resourse/무제2.txt','r',encoding='utf-8') as f:
        line = f.readline()
        print(line)
except FileNotFoundError as e:
    print('지정된 경로에 파일이 존재하지 않습니다.')

print('end 정상종료')