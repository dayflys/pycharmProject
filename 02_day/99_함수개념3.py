'''
    함수의 기본 개념
'''

#두 개의 문자열 연결하는 함수
#사용자 지정 함수 만들어 보기
def str_concat(s1,s2):
    s_result = s1+s2
    return s_result

result = str_concat("hello ",'world')
print(result)


result = str_concat("java ",'python')
print(result)