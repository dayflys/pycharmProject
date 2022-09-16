'''
    함수의 기본 개념
'''

#두 개의 문자열 연결하는 함수
#default parameter
def str_concat(s1,s2=''):#default 값을 지정할 수 있다. 값이 들어오면 그 값을 아니면 default값을 사용한다.
    s_result = s1+s2
    return s_result

result = str_concat("hello ",'world')
print(result)

result = str_concat("java ",'python')
print(result)

result = str_concat("java ")
print(result)