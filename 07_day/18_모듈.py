'''
    모듈(module)
    -> .py 파일 하나를 모듈이라고 칭한다
    -> 이는 독자적으로 실행이 가능하다.

    1.개념
    -> 파이썬 파일 하나를 의미 한다
    ex) a.py(모듈),b.py(모듈)
    -> 이 파일(모듈)이 모여서 하나의 폴더(패키지)가 된다.
        => 패키지를 왜 만드는 가? 모듈 관리를 위해서

    모듈(module)과 패키지(pakage)
    1.  python -> 패키지 -> 모듈
        windows-> 폴더  -> 파일

    2. 파이썬의 모듈들은 개별적으로 실행이 가능하다.(자바는 독자적인 실행은 불가능하다. 자바는 'main'메서드를 가진 파일만 실행할 수 있다.)
        => 'main'이라고 하는 메서드 역할은 시작점 역할을 한다. 이는 한 파일에만 존재해야한다.

    3.예) 애완 동물 관리 프로그램을 만들었다고 가정
    모듈 간에는 직접 접근이 불가능 하다 => 이유: 보안 때문에
    따라서 패키지 간에는 직접 접근이 불가능하다.
    그렇기에 간접 접근을 해야 하는데 이 때 쓰는 키워드 => import


'''