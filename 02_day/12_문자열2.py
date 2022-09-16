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

    2. 문자열 종류 2가지
    가.bytes 타입의 문자열 ==> (바이너리 기반)
    예) b"hello", b"홍길동"
    
    ===> 크롤링(인터넷에 돌아다니는 임의의 데이터를 수집하는 것) 시 넘어오는 데이터는 bytes 타입로 넘어온다
    
    나. (Unicode) 문자열 -> 우리가 쓰는 문자열 => 텍스트 기반
    예) "hello", "홍길동"
'''

#1. (유니코드) 문자열,
#  default encoding = utf-8(Unicode Type Format) => 전세계 모든 문자 표현가능
#  errors = 'strict'
s = 'hello홍길동'#암호화
s2= s.encode()
print(s,s2) #hello홍길동 b'hello\xed\x99\x8d\xea\xb8\xb8\xeb\x8f\x99'
print(type(s), type(s2)) #<class 'str'> <class 'bytes'>
'''
    <class 'str'> <class 'bytes'>
        'hello' ---> b'hello' <-- encode()
        'hello' ---> b'hello' <-- decode()
'''
#복호화
print(dir(bytes)) # <= str과 구성요소는 비슷하다. 다만 decode 가 있고 encode는 없다.

