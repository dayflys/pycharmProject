'''

    sample01.py
    -module01.py 접근하는 용도

    1) 경로지정
        import 패키지명.모듈명
        import 패키지명.모듈명 as 별칭

'''

import mymodule.module01 as x #as 를 사용해서 별칭을 줄 수 있다. 아니면 기존 모듈 이름을 사용해도 상관 없다.
import mymodule.module02 as y

#모듈들이 독립적으로 다 실행이 가능하지만 시작점 역할 코드를 지정하고 다른 모듈을 사용하면, 다른 이로 하여금 이 모듈이 시작 모듈임을 알 수 있다.

print(__name__)

if __name__ == '__main__':
    c = x.num
    x.fun()
    c1= x.Cat()
    print(id(x.Cat))

    d = y.num2
    y.fun2()
    d1= y.Dog()
    print(id(y.Dog))

