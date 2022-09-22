'''

'''

class Cat:
    x = 10 #클래스 변수 ===> 접근방법 2가지(내부 : cls.x, 내외부: Cat.x)

    @classmethod
    def y(cls):#class 메서드 ==> 접근방법 2가지(내부 : cls.y(), 내외부: Cat.y())
        print('x 값 접근1:', cls.x) #x 값 접근1: 10
        print('x 값 접근2:', Cat.x) #x 값 접근2: 10
        # print(self) #에러이유는 클래스 변수 및 메서드가 인스턴스(self) 보다 먼저 생성 되기 때문이다.

    def k(self):
        print('k에서 x접근',Cat.x) #실행되는 이유는 인스턴스 메서드(k)보다 클래스 변수(x)가 먼저 생성되기 때문이다.
        # print('k에서 x접근',cls.x)#인스턴스 메서드 안에서는 클래스 변수를 cls로 참조 불가능 => parameter 에 없으니까

Cat.y()
print(Cat.x)#10

c1 = Cat()
c1.k()


