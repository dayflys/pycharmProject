'''
    dict comprehension(dict + for문 + if)
    1.dict + for문 결합
    => 변수 = { k:v for k,v in dict.items()}

    2.dict + for문 결합 + 단일 if문
    => 변수 = { k:v for k,v in dict.items() if 조건식}

    3.dict + for문 결합 + if~else문
    => 변수 = { 참 if 조건식 else 거짓 for k,v in dict.items()}

'''

#1.dict + for문 결합
m = {'name':'홍길동', 'age':20,'address':'서울'}
result= { k:v for k,v in m.items()}
print(result)#{'name': '홍길동', 'age': 20, 'address': '서울'}

result= { v:k for k,v in m.items()}
print(result)#{'홍길동': 'name', 20: 'age', '서울': 'address'}

#2.dict + for문 결합 + 단일 if문
#key값의 길이가 4글자 이상인 값만 반환
result= {k:v for k,v in m.items() if len(k)>=4}
print(result)

#3.dict + for문 결합 + if~else문
#key값의 길이가 4글자 이상이면 key만, 아니면 value만 출력
result= {k if len(k)>=4 else v for k,v in m.items()}
print(result)#{'address', 20, 'name'}