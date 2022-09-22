'''

    상속(inheritance)
'''

#애완동물 관리 어플리케이션 개발 중(강아지와 고양이)
'''
    고양이 ============>   Cat
    속성: 이름, 나이, 성별    인스턴스 변수(생성자 이용해서 초기화)
    동작: 먹기, 자기, 뛰기
    강아지 ===========>    Dog
    속성: 이름, 나이, 색상    인스턴스 변수(생성자 이용해서 초기화)
    동작: 먹기, 자기, 수영
'''
class Cat:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def cat_eat(self):
        print('고양이 먹기')

    def cat_sleep(self):
        print('고양이 자기')

    def cat_run(self):
        print('고양이 뛰기')
    #getter와 setter 메서드 생략
class Dog:

    def __init__(self,name,age,color):
        self.name =name
        self.age =age
        self.color =color

    def dog_eat(self):
        print('강아지 먹기')

    def dog_sleep(self):
        print('강아지 자기')

    def dog_swim(self):
        print('강아지 수영')

c1 = Cat('야옹이',2,'암컷')
d1 = Dog('망치',2,'수컷')

print('고양이 정보= 이름: {}, 나이: {} 성별: {}'.format(c1.name,c1.age,c1.gender))
print('강아지 정보= 이름: {}, 나이: {} 색상: {}'.format(d1.name,d1.age,d1.color))

#고양이 액션
c1.cat_eat()
c1.cat_sleep()
c1.cat_run()

#강아지 액션
d1.dog_eat()
d1.dog_sleep()
d1.dog_swim()

'''
    상속 전 코드 문제점
    1. 코드 중복 ======> 해결: 중복 제거
        -동일한 속성들이 각 클래스마다 중복 된다.
        
    2. 메서드 명이 너무 많다. ==> 해결: 동일한 이름으로 
        -프로그램 관리가 어려워 진다.
'''



