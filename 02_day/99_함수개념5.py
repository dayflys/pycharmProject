'''
    함수의 기본 개념
'''

#두 개의 문자열 연결하는 함수
#s1,s2를 출력시 할당 할 수 있다
def str_concat(s1,s2):
    s_result = s1+s2
    return s_result

result = str_concat(s1= "hello ",s2='world')
print(result)

result = str_concat(s2="java ",s1='python')
print(result)
