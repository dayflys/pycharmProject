'''
    생성자(constructor)
    메서드(method)
        -꼭 검증 작업 때문에 메서드를 쓰는 것은 아니다.
'''

class Cat:
    #클래스 변수
    def __init__(self,username,age):#로컬변수
        print('__init__ 생성자')
        self.username = username#인스턴스 변수
        self.age = age#인스턴스 변수

    #age 변경하는 메서드
    def set_age(self,age):
        if age <= 20:
            self.age = age
        else:
            print('올바른 값을 입력하세요')

    #age 값을 반환하는 메서드
    def get_age(self):
        return self.age


c1 = Cat('야옹이',2)
#인스턴스 변수를 직접 접근해서 조회
print(c1.username)
print(c1.age)


c2 = Cat('나비',3)
print(c2.username)
print(c2.age)
#나비 age 수정 -> c2의 age(인스턴스 변수)에 직접 접근 해서 값을 수정
#c2.age = 4
c2.set_age(5)
print(c2.age, c2.get_age()) #5 5

'''

인스턴스 변수를 직접 조회, 수정하는 것은 권장하지 않음
이유는 올바른 데이터 저장이 안될 수 있다. => 현실적으로 말이 안되는 값도 저장이 되기 떄문
검증 할 수 있는 방법이 없어서 바로 저장이 된다.
해결은 일반 메서드(인스턴스 메서드)를 활용해서 검증 처리후 저장하도록 한다.

'''