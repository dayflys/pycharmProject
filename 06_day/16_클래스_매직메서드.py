'''
    매직 메서드 (magic method, 스페셜 메서드)

    1. __함수명__ 형식으로 구성됨
    2. 우리가 직접 호출하는 것이 아니고 특정 작업 진행시 자동 호출 된다.
    3.확인하는 방법
        print(dir(자료형)) 등등
    4. 결론은 필요할 때 매직 메서드를 overriding 해서 사용하자.

'''


#1. 클래스 생성할 때
class Cat:
    def __init__(self):#1. 클래스 생성할때
        print("__init__") #인스턴스 변수를 초기화할 목적으로 재정의 했다.


c1 = Cat()#__init__

#2.클래스 생성 후에 클래스를 참조하는 변수(c)를 출력할 때
class Cat:
    def __init__(self,username,age):
        self.username =username
        self.age =age

    def __str__(self):#자바의 toString() 메서드와 동일 기능
        return self.username+ str(self.age)

    # 가정: 함수 호출해서 username과 age 얻기
    def info(self):
        return self.username+ str(self.age)



c2 = Cat('야옹이',2)
print(c2.info()) #c2.info() 라는 함수호출해서 "야옹이2" 결과 ==> info() 메서드를 반드시 호출해야됨
print(c2) #c2.info() 라는 함수호출없이 그냥 c만 출력해서 "야옹이2" 결과값을 받음 (훨씬 편하게 원하는 데이터 얻을 수 있음)


#3. 함수처럼 호출 가능하도록 재정의 할 수 있다. ===> 여지껏 사용했던 코드들 중에서 호출할 수 있었던 것들은 모두 이 함수를 재정의한 것
#호출 여부 확인? callalbe(값) => 값이 호출할 수 있으면 True, 아니면 False 다.
# __call__
class Cat:
    pass

class Dog:
    def __call__(self):
        return '__call__'


print('str 호출 가능 여부: ', callable(str)) #str 호출 가능 여부:  True,str()가 가능 한 것
print('int 호출 가능 여부: ', callable(int)) #int 호출 가능 여부:  True,int()가 가능 한 것
print('list 호출 가능 여부: ', callable(list)) #list 호출 가능 여부:  True,list()가 가능 한 것
print('tuple 호출 가능 여부: ', callable(tuple)) #tuple 호출 가능 여부:  True,tuple()가 가능 한 것
print('dict 호출 가능 여부: ', callable(dict)) #dict 호출 가능 여부:  True,dict()가 가능 한 것
print('2 호출 가능 여부: ', callable(2)) #2 호출 가능 여부:  False,2()가 불가능 한 것

class Bird:
    def __call__(self,*n):
        return '__call__ '+str(n)

c = Cat()
d = Dog()
b = Bird()

print('Cat 호출 가능 여부: ', callable(c)) #Cat 호출 가능 여부 False,c()가 불가능 한 것
print('Dog 호출 가능 여부: ', callable(d), d()) #Dog 호출 가능 여부:  True __call__,d()가 가능 한 것
print('Bird 호출 가능 여부: ', callable(b), b('까마귀')) #Bird 호출 가능 여부:  True __call__ 까마귀,d()가 가능 한 것
print('Bird 호출 가능 여부: ', callable(b), b('까마귀','꿩')) #Bird 호출 가능 여부:  True __call__ ('까마귀', '꿩'),d()가 가능 한 것

