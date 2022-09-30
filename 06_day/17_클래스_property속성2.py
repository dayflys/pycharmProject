'''


    property(프라퍼티) 란?
    ==> 클래스 내의 메서드를 변수처럼 사용 가능 하다.
        이때, 사용되는 변수를 property라고 한다.

    class Cat:
        def __init__(self,name,age): #name, age ==> 로컬 변수
            self.name = name # self.name => 인스턴스 변수
            self.age = age # self.age => 인스턴스 변수

        def get_name(self): #getter 메서드
            return self. name

        def set_name(self,name): #setter 메서드
            self.name = name

        #getter 메서드와 setter 메서드 ===> xxx (property)
        ==> xxx 하나로 getter와 setter 를 전부 할 수 있다.

        -> property 만드는 방법 두 가지
        1. property 변수명 = property(메서드명, 메서드명)
        => 메서드에는 모든게 들어갈 수 있다.
        => 다만 메서드가 선언되고 나서 선언해야 한다.

        2. decorator 이용하는 법
        ===> 메서드 명이 모두 동일해야 한다.

        @property
         def username(self):  # getter 메서드
        return self.name

        @uesrname.setter
        def username(self, name):  # setter 메서드
        self.name = name
'''

#xxx = 값 # setter 역할
#print(xxx) # getter 역할

#property 만드는 방법 1
class Cat:
    def __init__(self, name, age):  # name, age ==> 로컬 변수
        self.name = name  # self.name => 인스턴스 변수
        self.age = age  # self.age => 인스턴스 변수

    @property
    def username(self):  # getter 메서드
        return self.name

    @username.setter
    def username(self, name):  # setter 메서드
        self.name = name

c = Cat('홍길동',20)
print('name 값 얻기: ', c.name, c.username) #name 값 얻기:  홍길동 홍길동

c.username = '유관순'
print('name 값 얻기: ', c.name, c.username) #name 값 얻기:  유관순 유관순
