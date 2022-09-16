
'''
    함수 
    -> 목적: 기능 처리
    
    1. 시스템 제공한 함수
    
    2. 사용자 정의 함수
        def 함수명():# 함수 header
            (작업) #body
            return 리턴값 #foot
    -> 함수는 호출을 해야 실행됨 => 함수명()
    -> 함수는 호출해야 실행되고 실행 후에는 호출한 곳을 돌아온다 -> return 한다고 한다.
'''

'''
    함수의 기본 개념
'''
print(1)
def fun(): #header
    print('fun', end='\n')#이 함수의 body 부분,
    return 100 # footer
print(1)
fun()
