'''
    제어문(반복문)

    1. for문

        for 변수 in 집합형: => 집합형 개수만큼 반복됨
            문장

        가. 일정 횟수 반복 용도
        ===> range() 함수 이용해서 개수를 만들어 준다. => builtins 객체

        나. 집합형 데이터를 조회용 반복
        ==> enumerate() 함수 이용해서 반복 횟수 값을 얻을 수 있다. => builtins 객체

    2. while 문

'''
#5개의 요소를 가진 집합형을 만든다.
#반복 횟수가 중요한 경우에는 dummy variable을 사용할 수 있다.
# for n in "hello":
#     print('hello')
#
# for n in [1,2,3,4,5]:
#     print('hello')

for _ in (1,2,3,4,5):
    print("hello")

print((range(10)))#range(0, 10) -> 반환 형이 range object기 때문에 출력결과가 이렇다.
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in range(5):
    print("world")

for x in range(1,6):
    print("kkk",x)

for x in range(1, 11,2):
    print('zzz', x)
#help(range)
'''
range(stop) -> range object
range(start, stop[, step]) -> range object
 '''

#나. 집합형 데이터를 조회용 반복
#num = [10,4,6,78]
#num = 'hello'
num = {'name': "홍", 'age': 20} #key값이 반복 된다.
for n in num:
    print(n) # 10 4 6 78

#num = [10,4,6,78]
for n in enumerate(num):
    print(n)# 반복 인덱스와 값을 튜플 값으로 출력해준다.

for idx, key in enumerate(num):
    print(idx, key)# 반복 인덱스와 값을 튜플 값으로 출력해준다.

for idx, key in enumerate(num,1):#enumerate 함수에 시작 값을 지정할 수 있다. 두 번째 인자로 들어가며 아무숫자나 줄수 있다.
    print(idx, key)# 반복 인덱스와 값을 튜플 값으로 출력해준다.

# help(enumerate) #enumerate(iterable, start=0)