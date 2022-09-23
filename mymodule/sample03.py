'''

    sample01.py
    -module01.py 접근하는 용도

    1) 경로지정
        import 패키지명.모듈명
        import 패키지명.모듈명 as 별칭

    2) 경로지정
        from 패키지명 import 모듈명 => 이렇게 선언한다면 모듈명만으로 사용이 가능하다

    3) 경로지정 (권장 안함) => 가독성이 너무 떨어진다.
        from 패키지명.모듈명 import 요소이름

'''

# from mymodule import module01
# from mymodule import module02
# from mymodule import module01,module02
# from mymodule import module01 as x #as 를 사용해서 별칭을 줄 수 있다. 아니면 기존 모듈 이름을 사용해도 상관 없다.
# from mymodule import module02 as y #as 를 사용해서 별칭을 줄 수 있다. 아니면 기존 모듈 이름을 사용해도 상관 없다.
from mymodule.module01 import Cat,fun,num
from mymodule.module02 import Dog,fun2,num

c = Cat()
fun()
print(num)
d = Dog()
fun2()

