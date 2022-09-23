
class Pet:

    def __init__(self,username,age): #공통적인 속성을 추출해서 부모인 Pet에서 선언한 것
        self.username =username
        self.age =age

class Cat(Pet):

    def __init__(self,username,age,gender):#이름, 나이, 성별 3가지 속성을 가진 Cat
        #self.username =username
        #self.age =age
        super().__init__(username, age) #부모생성자를 호출하면서 부모를 먼저 생성함
                                        #동시에 부모에서 선언된 username과 age 값을 초기화 하기 위해서
                                        #로컬 값을 전달함
        self.gender =gender

    def cat_print(self):
        print(self.username, self.age,self.gender)

    def __str__(self):
        return self.username + str(self.age) + self.gender

c1= Cat('야옹이',2 ,'암컷')
c1.cat_print()
print(c1) # __str__ 자동호출 ==> 결과 값: 야옹이2암컷
#계층구조
print(Cat.mro())

'''
    object 클래스
    class Pet: => () 없는 클래스는 자동으로 Object를 상속 받는다.
    
    객체의 계층 구조를 파악하는 함수
    인스턴스.mro
'''
