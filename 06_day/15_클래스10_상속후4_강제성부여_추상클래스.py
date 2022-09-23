'''

    추상클래스 (abstract class)
    1. abstract(추상적인) 의미: 구체와 되지 않음을 의미
    2. 특징:
        -메모리에 못 올라간다. 즉, 객체 생성이 불가능하다. => 객체생성 코드를 작성할 수 없다.
        -추상 메서드(abstract method)를 갖는다.
        ===> 자식 클래스에서 반드시 사용해야 되는 메서드를 추상 메서드로 만든다.
            @abstractmethod
            def eat(self):
                pass
            ===> 상속받은 자식클래스에서 부모의 추상메서드를 반드시 재정의 해야 자식을 객체 생성 할 수 있다.
    3. 문법
        from abc import ABC,abstractmethod

        class Pet:
        ===> 일반 클래스
        ===> p = Pet() #객체생성 가능
        class Pet(ABC):
        ===> 추상 클래스
        ===> p =Pet() #객체 생성 불가

        @abstractmethod
'''
from abc import ABC,abstractmethod

class Pet(ABC):
    @abstractmethod
    def eat(self):
        pass

class Cat(Pet):
    def eat(self):
        print("Cat eat")

class Dog(Pet):
    def eat(self):
        print("Dog eat")
# p = Pet() #Pet은 추상메서드를 포함한 추상클래스이기 때문에 객체 생성 불가
c = Cat()
c.eat()

d = Dog()
d.eat()