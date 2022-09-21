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

    3.else
        ===> 반복문 사용시 정상적인 방법으로 종료여부 확인 가능
        ( 비정상적인 방법:break 사용시 가정)
        ==> 어떻게 반복문이 종료 되는지를 알고자 할 때 쓰는 문장
        ==> break 정상 작동 시, else 문은 실행 되지 않음
'''

print('start')

for n in range(5):
    if n == 3: break
    print(n)
else:
    print('정상종료')

print('end')

