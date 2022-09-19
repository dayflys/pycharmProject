'''
    제어문(반복문)

    1. for문

        for 변수 in 집합형: => 집합형 개수만큼 반복됨
            문장

        가. 일정 횟수 반복 용도
        ===> range() 함수 이용해서 개수를 만들어 준다.

        나. 집합형 데이터를 조회용 반복

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