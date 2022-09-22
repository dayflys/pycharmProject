'''

    상속(inheritance) 방법

    1. 공통적인 속성 및 동작을 추출해서 새로운 클래스로 작성한다. => 코드의 재사용 목적
        -이 클래스는 기존의 존재하는 클래스(강아지, 고양이)를 개념적으로 포함하는 클래스(애완동물 pet)로 작성해야 한다.

        pet(부모 클래스) is a 관계  <- cat(자식 클래스)
                      is a 관계  <- dog(자식 클래스)

    2. 부모를 참조하는 방법 => 부모를 가리키는 키워드는 super()를 이용한다.
        => super().요소
        => super().메서


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
#1.공통적인 속성 및 동작을 추출해서 새로운 클래스로 작성한다.
class Pet:
    def __init__(self,name,age):
        self.age =age
        self.name =name

class Cat(Pet):
    def __init__(self,name,age):
        self.age =age
        self.name =name

    def cat_print(self):
        print(self.name,self.age)


class Dog(Pet):
    def __init__(self,name,age):
        self.age =age
        self.name =name

    def dog_print(self):
        print(self.name,self.age)

p1 = Pet("망치",2)
c1 = Cat("망치",2)
d1 =Dog("망치",2)
c1.cat_print()
d1.dog_print()