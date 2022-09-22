'''
    클래스 메서드

    1. 문법
        class 클래스명:

            @classmethod #@-> 파이썬에서 decorator 라고 하고 자바에서는 annotation이라고 한다
            def 클래스메서드명(cls):
                pass
            ---> 인스턴스와 무관하며, 프로그램 실행시 생성 ~ 프로그램 종료시 제거
            ==> 사용 방법:
                    클래스명.클래스메서드() 형식으로 사용한다.
            ===> 용도:
                -객체 생성없이 메서드 사용하기 위해서 (**********)

            def 인스턴스메서드(self):
                pass
            --> 객체 생성시 인스턴스 메서드가 생성됨 (객체 생성 후에 사용이 가능하다.)
            ---> 사용방법: self.인스턴스메서드
                        c1.인스턴스 메서드
            => 중요한 것은 객체 생성을 꼭 해야한다는 것이다.

'''

class Cat:

    x = 10 #클래스 변수

    @classmethod
    def kkk(cls):
        print('cls 주소값:', id(cls))
        print('kkk')

    def a(self):
        print('self 주소값:',id(self))
        self.b()#같은 클래스내에서 인스턴스 메서드 호출은 self.메서드명 (인스턴스 변수사용과 동일)
        print('a')

    def b(self):
        print('b')

Cat.kkk() #객체 생성전에 사용 가능하다.

c1 = Cat()
c1.a()
print('c1 주소값:',id(c1))
print('c1 주소값:',id(Cat))



