'''
    멤버쉽연산자
    - 집합형에서 데이터 존재 여부 확인

    -변수 = 값 in 집합

'''

result = 10 in [10,20,30]
print(result)#True
result = 10 in (10,20,30)
print(result)#True
result = 10 in {10,20,30}
print(result)#True

print(200 in [10,20,30])#False

m_dict = {'x':100, 'y':200, 'z':300}
print('x' in m_dict) #True
print('a' in m_dict) #False