'''
    반복문에서 사용하는 키워드

    1.break
        ==> 반복문을 빠져나올 때 사용
        ==>
            for 문:
                if 조건:break
                문장

    2.continue
        ==> 반복 처리되는 여러 문장들 중에서
            특정 반복 횟수에서 특정 문장들을 skip 하고자 할 때 사용



'''

print('start')

for n in range(5):
    print('반복처리문 1')
    print('반복처리문 2')
    if n == 3: continue
    print(n)
    print('반복처리문 3')

print('end')

'''
start
반복처리문 1
반복처리문 2
0
반복처리문 3
반복처리문 1
반복처리문 2
1
반복처리문 3
반복처리문 1
반복처리문 2
2
반복처리문 3
반복처리문 1
반복처리문 2
반복처리문 1
반복처리문 2
4
반복처리문 3
end
'''

#1~10 까지 반복하는데 짝수만 출력
print('실습 start')
for x in range(1,11):
    if x%2 != 0:
        continue
    print(x)
print('실습 end')

'''
실습 start
2
4
6
8
10
실습 end
'''