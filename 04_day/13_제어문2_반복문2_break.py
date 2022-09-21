'''
    반복문에서 사용하는 키워드

    1.break
        ==> 반복문을 빠져나올 때 사용
        ==>
            for 문:
                if 조건:break
                문장


'''

print('start')

for n in range(5):
    if n == 4:
        break
    print(n)

print('end')


'''
start
0
1
2
3
end
'''