'''
   표준 입력
   1. input() 함수 이용
   help(input)
   input(prompt=None, /)
    Read a string from standard input.=> 표준 입력: 키보드
    -> 읽으면 str 값으로 읽어 온다.

    2. '20' --> 20 변환함수
    int('20') --> 20
'''
# help(input)

#표준 입력인 키보드의 값을 받아서 데이터를 생성한다. 이때 생성된 데이터의 클래스는 str 이다.

name =input("이름을 입력 하시오")
print('입력된 이름:',name)
age = input('나이 입력: \n')
print('내 이름:',name, type(name))
print('내 나이:',age, type(age))
print('내년 나이: ',int(age)+1, type(age),type(int(age)))
