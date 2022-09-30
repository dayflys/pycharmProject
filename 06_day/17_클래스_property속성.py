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
'''

#xxx = 값 # setter 역할
#print(xxx) # getter 역할

#property 만드는 방법 1
class Cat:
    def __init__(self, name, age):  # name, age ==> 로컬 변수
        self.name = name  # self.name => 인스턴스 변수
        self.age = age  # self.age => 인스턴스 변수

    def get_name(self):  # getter 메서드
        return self.name

    def set_name(self, name):  # setter 메서드
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

    #property 설정
    username = property(get_name,set_name)
    userage = property(get_age,set_age)

c = Cat('홍길동',10)
print('c.name 값 얻기: ',c.name, c.get_name(), c.userage) #홍길동 홍길동 홍길동

#name 수정
c.name = "이순신"
print(c.name) #이순신
c.set_name("유관순")
print(c.name) #유관순
c.username = '강감찬'
print(c.username) #강감찬

print('c.age 값 얻기: ',c.age, c.get_age(), c.userage) #c.age 값 얻기:  10 10 10

#age 수정
c.age = 20
print(c.age) #20
c.set_age(30)
print(c.age) #30
c.userage = 40
print(c.userage) #40
