'''
    list comprehension(리스트 + for문 + if)
    1.리스트 + for문 결합
    -> 리스트에서 반복적으로 값을 추출 + 가공해서 다시 리스트로 변환
    -> 리스트 + for문 결합
    => 변수 = [ 표현식 for 변수 in 리스트]

    2.리스트 +for문  결합 + 단일 if문
    변수 = [ 표현식 for 변수 in 리스트 if 조건식]

    3.리스트 +for문  결합 + if~else문(삼항 연산자)
    변수 = [ 참 if 조건식 else 거짓 for 변수 in 리스트]

'''

#1. 리스트 + for 문 결합
result=[v for v in range(5)]
print(result) #[0, 1, 2, 3, 4]

result=[v+1 for v in range(5)]
print(result) #[1, 2, 3, 4, 5]

result=[[v + 1] for v in range(5)]
print(result) #[[1], [2], [3], [4], [5]]

result=[[v, v+1, 0] for v in range(5)]
print(result) #[[1], [2], [3], [4], [5]]

print('*'*40)

#2.리스트 +for문  결합 + 단일 if문
#1~10 사이에서 짝수만 출력
result = [v for v in range(1,11) if v%2 == 0]
print(result)

print('*'*40)

#3.리스트 +for문  결합 + if~else문
#1~10 사이에서 짝수만 0, 홀수면 1 출력
result = [0 if v%2 == 0 else 1 for v in range(1,11) ]
print(result)
