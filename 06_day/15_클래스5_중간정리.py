'''
    분석단계

    고양이 객체 추출 ===> 클래스
    속성: 이름, 나이, 성별 ====> 인스턴스 변수
    동작: 먹기,자기, 나이 변경 ====> 인스턴스 메서드

    실제 고양이 2마리
    -야옹이,2,암컷
    -나비,3,수컷
'''

'''
    1. 로컬 변수 
        ===> self없는 변수들
        ===> 용도: 임시적으로 임의의 값을 저장할 때 쓴다.
        ===> 메서드 호출할때마다 생성~ 메소드 실행이 끝날 때 제거
        
    * 로컬 변수
    def a():
        b(n)
    def b(x):
        print(x)
        
    a(10)
    2. 인스턴스 변수
        ===> self 있는 변수들 
        ===> 용도: 고양이(객체)의 속성 정보저장(이름, 나이 ,성별)
        ====> 객체생성마다 매번 생성~ 객체 소멸할 때 제거
    
    *객체 소멸 시점
    ===> 참조하는 변수가 없을 때
    
    c1 = Cat('야옹이',2)
    c2 = Cat('나비',2)
    c1 = Cat('이쁜',3) # c1에 다른 인스턴스를 할당한다면 Cat('야옹이',2)라는 객체는 소멸 한다.
    
    3. 클래스 변수
    
    python - 메서드 안 -로컬 변수
                    -인스턴스 변수
           - 메서드 밖- 클래스 변수
           
    자바- 메서드 안 - 로컬 변수
       - 메서드 밖 - 인스턴스 변수
                - 클래스 변수
                
                
    class 클래스 명:
        변수명 = 값 #클래스 변수
        def __init__(self,username): #로컬 변수
            self.username = username #인스턴스 변수 
            
    클래스 변수 특징
    => 단한번만 생성됨 -> when? 프로그램 실행 시 생성 ~ 프로그램 종료 시 소멸
    -> 가장 오래 사는 변수 => 누적용으로 적합
    -> 객체 생성 전에 만들어짐 (객체 생성 무관 )-> 인스턴스 무관 -> self 사용 불가(자바에서는 this)
    => 접근 방법: 
            클래스명.변수명
    
    
'''
class Cat:
    #생성자 ==> 역할: 인스턴스 변수 초기화
    def __init__(self,name,age,gender): #로컬 변수, stack 메모리에 생성
        #인스턴스 변수, heap 메모리에 저장 됨
        self.name = name
        self.age= age
        self.gender = gender

    #setter 메서드
    def eat(self):
        #검증처리
        print(f'{self.name} 밥먹는다.')

    def sleep(self):
        #검증처리
        print(f'{self.name} 잔다')

    def set_age(self,age):
        #검증처리
        self.age = age

    #getter 메서드
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

c1= Cat("야옹이",2,"암컷")#객체 소멸된다. 이유는 참조하는 변수가 없기 때문이다.
c2= Cat("나비",3,"수컷")
c1= Cat("이쁜",1,"암컷")
c1.eat()
c1.sleep()
#조회 1 - 직접 인스턴스 변수 접근
print('고양이 1 정보: 이름:{}, 나이:{}, 성별:{}'.format(c1.name,c1.age,c1.gender))
print('고양이 2 정보: 이름:{}, 나이:{}, 성별:{}'.format(c2.name,c2.age,c2.gender))

#조회 2 - 메서드를 이용한 접근
print('고양이 1 정보: 이름:{}, 나이:{}, 성별:{}'.format(c1.get_name(),c1.get_age(),c1.get_gender()))
print('고양이 2 정보: 이름:{}, 나이:{}, 성별:{}'.format(c2.get_name(),c2.get_age(),c2.get_gender()))
