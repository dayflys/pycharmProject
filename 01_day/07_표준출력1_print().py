'''
    표준 출력
    1.print() 함수 이용
    help(print)
    print(value, ..., sep=' ', end='\n', file=sys.stdout(표준출력 즉, 모니터), flush=False)
'''

#help(print)

#1. 값을 여러개 사용가능
print(10)
print(10,20,30)

#2.여러 값 출력 시, 기본자는 기본적으로 공백 적용 ==> 커스터마이징 가능
print(10,20,30)#10 20 30
print(10,20,30, sep=',')#10,20,30

#3. print 기본적으로 개행이 된다. 즉 새로운 줄에 출력이 된다. ==> 커스터마이징 가능
print(10)
print(20)
print(30)
print(10,20,30,end='\n')
print(10,20,30,end='\t')
print('그 다음 줄')

#4. 모두 적용 가능
print(1,2,3, sep=':',end=' ')
print(10,20,30)

#5. 모니터의 출력 대신에 파일에 출력 가능, 이 때 f는 별칭이며 file = 별칭으로 실행 된다.여긴 다시 공부해보자
with open('../a.hwp','w') as f:
    print("helloworld", file = f)