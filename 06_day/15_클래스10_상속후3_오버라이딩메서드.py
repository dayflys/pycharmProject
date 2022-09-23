'''
    오버라이딩 메서드(overriding method)
    개념:
        부모에 있는 메서드를 그냥 사용하지 않고 수정(재정의) 후 사용하는 메서드를 의미한다

    목적:
        부모 메서드의 재사용, 관리하기 용이하게끔

        class Pet:
            def a(self):
                print("hello")

    *오버라이딩 메서드
    -> 메서드명은 동일 + 구현 코드는 변경

    *아쉬운 점은 강제성이 없다. 자식 클래스가 이전처럼 맘대로 메서드를 만들어서 사용해도 무관하다.
    ====> 해결 방법: 추상 클래스 --> 파이썬에서는 인터페이스가 없다
                (자바: 추상클래스, 인터페이스)

'''
class Pet:
    # 공통적인 속성 추출
    def __init__(self,username,age): #공통적인 속성을 추출해서 부모인 Pet에서 선언한 것
        self.username =username
        self.age =age

    #공통적인 기능 추출
    def eat(self):
        print('Pet eat')
        print('{}가 먹는다'.format(self.username))

    def pet_print(self):
        print(self.username,self.age)
class Cat(Pet):

    def __init__(self,username,age,gender):#이름, 나이, 성별 3가지 속성을 가진 Cat
        #self.username =username
        #self.age =age
        super().__init__(username, age) #부모생성자를 호출하면서 부모를 먼저 생성함
                                        #동시에 부모에서 선언된 username과 age 값을 초기화 하기 위해서
                                        #로컬 값을 전달함
        self.gender =gender

    def pet_print(self):
        print(self.username, self.age,self.gender)

    #고양이가 먹는 동작
    #overriding 메서드 -> 부모에 있는 eat 메서드를 재정의
    def eat(self):
        print('Cat eat')


class Dog(Pet):
    def __init__(self,username,age,color):
        super().__init__(username,age)
        self.color =color

    def pet_print(self):
        print(self.username,self.age,self.color)

    #오버라이딩 메서드 ==> 재사용이 되기 때문에 일관된 메서드(기능)를 사용 가능하다.
    def eat(self):
        print('Dog eat')


c1= Cat('야옹이',2 ,'암컷')
c1.pet_print()
c1.eat()

d1 = Dog('멈머',4,'흰색')
d1.pet_print()
d1.eat()

# #계층구조
# print(Cat.mro())
