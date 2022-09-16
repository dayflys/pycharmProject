"""
    문자열
    -> 부분값 구하기(색인) -> 방 번호로 구한다(순방향,역방향)
        인덱싱 : 값 하나만 구하기
        슬라이싱: 범위로 여러개 구하기
    -> 0부터 시작한다.(순방향)
    -> -1부터 내려간다(역방향)

    부분열 구하기
    -5 -4 -3 -2 -1(역방향)
     h  e  l  l  o
     0  1  2  3  4(순방향)

     s = h e l l o
     슬라이싱 s[start(순,역 둘다 가능):end(순, 역 둘다 가능)] => end-1까지 나온다.
     -> 순방향 start를 썼으면 순방향 end,
     -> 역방향 start를 썼으면 역방향 end <- 역방향은 start와 end를 반대로 써야 한다.
     -> start와 end는 생략도 가능하다, 이 때 생략하면, start는 0, end는 끝까지가 된다.

     s[start:end:step]
"""

s='hello'
#1.인덱싱 -> 문자 하나 색인
#2.슬라이싱 -> 범위로 지정
#순방향
print(s[0:3])#hel
print(s[2:4])#ll
print(s[:4])# hell
print(s[2:])# llo
print(s[:])# hello
#역방향
print(s[-3:-1])# ll
print(s[:-1])# hell ==> 처음부터 마지막 전까지
print(s[-3:])# llo

#step
s= 'sequence'
print(s[::2])#sqec
print(s[::-1])#ecneuqes